import pandas as pd
import matplotlib.pyplot as plt
import sys

def read_json_to_dataframe(in_file):
    print(f'Reading JSON file {in_file}')
    eva_df = pd.read_json(in_file, convert_dates=['date'])
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df



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
    data = read_json_to_dataframe(input_file)

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


   