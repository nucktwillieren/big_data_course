from tkinter.filedialog import askopenfilename
import datetime

def input_process_base(input_hint, func=None):
    """[summary]
    The input should be like 20180101, 20180102, 20180103
    """
    try:
        data = [d.strip() for d in input(input_hint).split(",")]
    except:
        raise ValueError("Invalid Format of Data", data)
    
    result = []
    if func:
        for d in data:
            try:
                result.append(func(d))
            except:
                print("Invalid Query String in Input, and We Will Ignore It", d)
    else:
        result = data

    return result

def datetime_convert(d):
    """[summary]
    Args:
        d ([str]): [%Y%m%d string time]

    Returns:
        [datetime.datetime]: [datetime object]
    """
    try:
        return datetime.datetime.strptime(d, "%Y%m%d") 
    except:
        raise ValueError(f"Invalid Datetime Format {d}" ) 

def datetime_station_mixed_convert(d):
    """[summary]
    Args:
        d ([str]): [ex: date_station]

    Returns:
        [tuple]: [ex: (date, station) This is for datetime format checking.]
    """
    try:
        date, station = tuple(d.split("_"))
        date = datetime_convert(date)
        return date, station
    except:
        raise ValueError("Invalid Datetime Station Mixed Format, and We Ignore It ", d)        

def same_date_serialize(date, station):
    result = []
    for d in date:
        for s in station:
            result.append((d, s))
    return result

def get_station_input():
    """[summary]
    The input should be like 台東, 山里, 鹿野, 瑞源
    """
    return input_process_base("Stations(Ex:台東, 山里, 鹿野, 瑞源): ")

def get_date_input():
    """[summary]
    The input should be like 20180101, 20180102, 20180103
    """
    return input_process_base("Date(Ex:20180101, 20180102, 20180103): ", datetime_convert)

def get_simple_mixed_input():
    """[summary]
    The input should be like 20180101_台東, 20180102_台東, 20180101_山里, 20180101_鹿野, 20180101_瑞源
    """
    data = input_process_base(
        "Input(Ex:20180101_台東, 20180102_台東, 20180101_山里, 20180101_鹿野, 20180101_瑞源): ",
        datetime_station_mixed_convert
    )
    return data

def get_the_same_date_input():
    date = get_date_input()
    station = get_station_input()
    return same_date_serialize(date, station)

class StationInfo:
    @classmethod
    def de_serialize(cls, arg_list=None, mapping=None):
        if mapping:  
            return cls(**mapping)
        if arg_list:
            return cls(*arg_list)

    def __init__(self, date, tkt_beg, name, inflow, outflow):
        #BOARD_DATE,TKT_BEG,STOP_NAME,進站,出站
        self.date = datetime_convert(date)
        self.tkt_beg = int(tkt_beg)
        self.name = name
        self.inflow = int(inflow)
        self.outflow = int(outflow)

    def __repr__(self):
        return f"{self.name} on {self.date}: Inflow={self.inflow} Outflow={self.outflow}"

    def __str__(self):
        return f"{self.name} on {self.date}: Inflow={self.inflow} Outflow={self.outflow}"

class StationInfoManager:
    def __init__(self, filepath, save_path):
        self.path = filepath
        self.save_path = save_path
        self.info_dict = {}
        self.read_file()

    def read_file(self):
        with open(self.path, encoding="utf-8") as f:
            f.readline()
            for line in f:
                try: # To avoid the error when readling lines
                    info = StationInfo.de_serialize(line.split(","))
                    self.info_dict[f"{info.date}_{info.name}"] = info
                except:
                    print("Error Occur When reading csv. Error in Line: ", line)

    def recreate_save_file(self):
        with open(self.save_path, "w", encoding="utf-8") as f:
            pass

    def write_save_file(self, results):
        with open(self.save_path, "a+", encoding="utf-8") as f:
            for r in results:
                f.write(str(r)+"\n")

    def search(self, query_set):
        """[summary]
        Args:
            query_set (list of tuple): [the query should be like [(datetime, station), .....]]
        """
        results = []
        for query in set(query_set):
            try:
                result = self.info_dict[f"{query[0]}_{query[1]}"]
                print(result)
                results.append(result)
            except KeyError:
                print("Invalid Searching Result(No such station on the specific date): ", query)
        
        return results
        
def main():
    filepath = askopenfilename()
    result_saving_path = "./train_station_flow_result.txt"

    a = StationInfoManager(filepath, result_saving_path)
    a.recreate_save_file()
    
    while 1:
        mode = input("Mode(simple/same_date):")
        if mode == "simple":
            while 1:
                results = a.search(get_simple_mixed_input())
                a.write_save_file(results)
        elif mode == "same_date":
            while 1:
                results = a.search(get_the_same_date_input())
                a.write_save_file(results)

if __name__ == '__main__':
    main()
    