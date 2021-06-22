filepath = "./week4/fileIO/map_areacodes_states.txt"

with open(filepath) as f:
    data = f.readlines()

with open("test.txt", "w") as w:
    w.writelines(data)

train_file_path = "./week4/fileIO/TrainStationFlow_2005-2017.csv"
with open(train_file_path, encoding="utf-8") as f:
    data = []
    for line in f:
        data.append(line.split(","))
    #print(data)
    header = data[0]
    print(header)