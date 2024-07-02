import pandas as pd
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':

    if len(sys.argv) < 3:
        input_file = './eva-data.json'
        output_file = './eva-data.csv'
        print(f'Using default input and output filenames')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print('Using custom input and output filenames')

    graph_file = './cumulative_eva_graph.png'

    print(f'Reading JSON file {input_file}')
    data = pd.read_json(input_file, convert_dates=['date'])
    data['eva'] = data['eva'].astype(float)
    # remove data entry with missing values
    data.dropna(axis=0, inplace=True)
    # sort data by the date column
    data.sort_values('date', inplace=True)

    print(f'Saving to CSV file {output_file}')
    data.to_csv(output_file, index=False)

    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    data['duration_hours'] = data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    data['cumulative_time'] = data['duration_hours'].cumsum()
    plt.plot(data.date, data.cumulative_time, 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()
    print("--END--")