import sys
import re
from datetime import datetime
import matplotlib.pyplot as plt

# Function to convert timestamp to seconds since start
def timestamp_to_seconds(timestamp, start_time):
    time_obj = datetime.strptime(timestamp, '[%H:%M:%S]')
    return (time_obj - start_time).total_seconds()

# Parse the log file
def parse_log_file(filename):
    species_data = {}  # {species: {id: [(time, biomass, energy)]}}
    species_names = set()  # Track unique species names
    start_time = None
    time_points = set()

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Extract timestamp
                timestamp_match = re.match(r'\[(\d{2}:\d{2}:\d{2})\]', line)
                if not timestamp_match:
                    continue
                timestamp = timestamp_match.group(0)
                if not start_time:
                    start_time = datetime.strptime(timestamp, '[%H:%M:%S]')
                time_seconds = timestamp_to_seconds(timestamp, start_time)
                time_points.add(time_seconds)

                # Extract species and instance (species name can be any string)
                species_match = re.search(r'([a-zA-Z0-9_]+)-(\d+)', line)
                if not species_match:
                    continue
                species, instance_id = species_match.groups()
                species_names.add(species)
                instance_key = f"{species}-{instance_id}"

                # Initialize species and instance if not exists
                if species not in species_data:
                    species_data[species] = {}
                if instance_key not in species_data[species]:
                    species_data[species][instance_key] = []

                # Parse biomass and energy updates
                grown_match = re.search(r'Grown to Size: (\d+\.\d{2}) Energy: (\d+\.\d{2}) Biomass: (\d+\.\d{2})', line)
                waste_match = re.search(r'-0\.5 energy down by waste! Energy: (\d+\.\d{2}) Biomass: (\d+\.\d{2})', line)
                reprod_match = re.search(r'Reproduced\. Spawning ([a-zA-Z0-9_]+)-(\d+) Energy: (\d+\.\d{2}) Biomass: (\d+\.\d{2})', line)
                death_match = re.search(r'([a-zA-Z0-9_]+)-(\d+) has died: Energy: [-\d+\.\d{2}] Biomass: (\d+\.\d{2})', line)
                consumed_match = re.search(r'([a-zA-Z0-9_]+)-(\d+) Consumed by ([a-zA-Z0-9_]+)-(\d+): New Energy: (\d+\.\d{2}) Biomass: (\d+\.\d{2})', line)

                if grown_match:
                    size, energy, biomass = map(float, grown_match.groups())
                    species_data[species][instance_key].append((time_seconds, biomass, energy))
                elif waste_match:
                    energy, biomass = map(float, waste_match.groups())
                    species_data[species][instance_key].append((time_seconds, biomass, energy))
                elif reprod_match:
                    new_species, new_id, energy, biomass = reprod_match.groups()
                    new_instance_key = f"{new_species}-{new_id}"
                    species_names.add(new_species)
                    if new_species not in species_data:
                        species_data[new_species] = {}
                    if new_instance_key not in species_data[new_species]:
                        species_data[new_species][new_instance_key] = []
                    species_data[new_species][new_instance_key].append((time_seconds, float(biomass), float(energy)))
                elif death_match:
                    dead_species, dead_id, biomass = death_match.groups()
                    dead_instance_key = f"{dead_species}-{dead_id}"
                    species_data[dead_species][dead_instance_key].append((time_seconds, float(biomass), 0.0))
                    # Remove instance after death
                    del species_data[dead_species][dead_instance_key]
                elif consumed_match:
                    consumed_species, consumed_id, consumer_species, consumer_id, new_energy, new_biomass = consumed_match.groups()
                    consumed_instance_key = f"{consumed_species}-{consumed_id}"
                    consumer_instance_key = f"{consumer_species}-{consumer_id}"
                    if consumed_instance_key in species_data[consumed_species]:
                        species_data[consumed_species][consumed_instance_key].append((time_seconds, 0.0, 0.0))
                    if consumer_species not in species_data:
                        species_data[consumer_species] = {}
                    if consumer_instance_key in species_data[consumer_species]:
                        species_data[consumer_species][consumer_instance_key].append((time_seconds, float(new_biomass), float(new_energy)))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return species_data, sorted(time_points), start_time, sorted(species_names)

# Calculate averages for plotting
def calculate_averages(species_data, time_points, species_names):
    avg_biomass = {species: [] for species in species_names}
    avg_energy = {species: [] for species in species_names}

    for time in time_points:
        for species in species_names:
            biomass_sum = 0
            energy_sum = 0
            count = 0
            if species in species_data:
                for instance, data in species_data[species].items():
                    # Find the latest data point before or at the current time
                    latest_data = None
                    for t, b, e in data:
                        if t <= time:
                            latest_data = (b, e)
                        else:
                            break
                    if latest_data and latest_data[1] > 0:  # Only count alive instances (energy > 0)
                        biomass_sum += latest_data[0]
                        energy_sum += latest_data[1]
                        count += 1
            # Calculate averages
            avg_biomass[species].append(biomass_sum / count if count > 0 else 0)
            avg_energy[species].append(energy_sum / count if count > 0 else 0)

    return avg_biomass, avg_energy

# Plot the data
def plot_data(time_points, avg_biomass, avg_energy, species_names):
    plt.figure(figsize=(12, 8))

    # Define colors for species (extendable for more species)
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'cyan']
    if len(species_names) > len(colors):
        print("Warning: More species than available colors. Some species may share colors.")
    
    # Plot average biomass
    plt.subplot(2, 1, 1)
    for i, species in enumerate(species_names):
        plt.plot(time_points, avg_biomass[species], label=f'{species} Biomass', color=colors[i % len(colors)])
    plt.xlabel('Time (seconds)')
    plt.ylabel('Average Biomass')
    plt.title('Average Biomass Over Time')
    plt.legend()
    plt.grid(True)

    # Plot average energy
    plt.subplot(2, 1, 2)
    for i, species in enumerate(species_names):
        plt.plot(time_points, avg_energy[species], label=f'{species} Energy', color=colors[i % len(colors)])
    plt.xlabel('Time (seconds)')
    plt.ylabel('Average Energy')
    plt.title('Average Energy Over Time')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    # Check if filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python plot_simulation.py <log_file_name>")
        sys.exit(1)

    filename = sys.argv[1]
    species_data, time_points, start_time, species_names = parse_log_file(filename)
    avg_biomass, avg_energy = calculate_averages(species_data, time_points, species_names)
    plot_data(time_points, avg_biomass, avg_energy, species_names)