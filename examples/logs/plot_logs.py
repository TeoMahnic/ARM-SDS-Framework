import matplotlib.pyplot as plt


def getData(filename:str)->list:
    # Open log file and read all data
    f = open(filename, 'r')
    data = f.read()
    f.close()

    data = data.strip('[]')
    data = data.split(',')
    data = [int(x) for x in data]
    trimData(data)

    return data

def trimData(data:list)->None:
    data_len = len(data)
    for i in range(1, data_len):
        if data[data_len - i] == 0:
            data.pop()
        else:
            break


def main()->None:
    interval = {}

    interval['temp0']  = getData('log_temperature0.txt')
    interval['accel0'] = getData('log_accelerometer0.txt')
    interval['gyro0']  = getData('log_gyroscope0.txt')
   
    interval['temp1']  = getData('log_temperature1.txt')
    interval['accel1'] = getData('log_accelerometer1.txt')
    interval['gyro1']  = getData('log_gyroscope1.txt')

    interval['temp_no_comp0']  = getData('log_temperature_no_comp0.txt')
    interval['accel_no_comp0'] = getData('log_accelerometer_no_comp0.txt')
    interval['gyro_no_comp0']  = getData('log_gyroscope_no_comp0.txt')
   
    interval['temp_no_comp1']  = getData('log_temperature_no_comp1.txt')
    interval['accel_no_comp1'] = getData('log_accelerometer_no_comp1.txt')
    interval['gyro_no_comp1']  = getData('log_gyroscope_no_comp1.txt')

    # Plot Temperature intervals
    plt.figure('Temperature')
    # plt.plot(interval['temp0'], label='Temperature 0')
    plt.plot(interval['temp1'], label='Temperature 1')
    # plt.plot(interval['temp_no_comp0'], label='Temperature no comp 0')
    plt.plot(interval['temp_no_comp1'], label='Temperature no comp 1')
    plt.legend()

    # Plot Accelerometer intervals
    plt.figure('Accelerometer')
    # plt.plot(interval['accel0'], label='Accelerometer 0')
    plt.plot(interval['accel1'], label='Accelerometer 1')
    # plt.plot(interval['accel_no_comp0'], label='Accelerometer no comp 0')
    plt.plot(interval['accel_no_comp1'], label='Accelerometer no comp 1')
    plt.legend()

    # Plot Gyroscope intervals
    plt.figure('Gyroscope')
    # plt.plot(interval['gyro0'], label='Gyroscope 0')
    plt.plot(interval['gyro1'], label='Gyroscope 1')
    # plt.plot(interval['gyro_no_comp0'], label='Gyroscope no comp 0')
    plt.plot(interval['gyro_no_comp1'], label='Gyroscope no comp 1')
    plt.legend()

    # Show plots
    plt.show()



if __name__ == '__main__':
    main()