import numpy as np 
import matplotlib.pyplot as plt 

# every line is a small company in a larger company
# every number represents how many products one person has made in one month

def file_handling():
    lines = []
    
    with open('company.txt', 'r') as file:
        for line in file:
            values = line.strip().split(",")
            int_values = [int(val) for val in values ]
            lines.append(int_values)
        
        data = np.array([np.array(row) for row in lines], dtype='object') 
        return data 

def productivity_of_company (data, order):
    return np.sum(data[order])

def max_productivity (data):
    i = 0 
    maxcomp = i+1
    maxprod = 0 
    for i in range(len(data)):
        result = productivity_of_company(data, i)
        if result > maxprod:
            maxprod = result
            maxcomp = i+1
    print(f"The company with maximum productivity in company nbr {maxcomp}, with {maxprod} product made")

def min_productivity (data):
    i = 0 
    mincomp = i+1
    minprod = productivity_of_company(data, 0) 
    for i in range(len(data)):
        result = productivity_of_company(data, i)
        if result < minprod:
            minprod = result
            mincomp = i+1
    print(f"The company with minimum productivity in company nbr {mincomp}, with {minprod} product made")

def plotting(data, order):
    x = np.arange(len(data[order]))
    plt.plot(x, data[order], marker = 'o')
    plt.title('Productivity of the workers')
    plt.xlabel('Worker tag')
    plt.ylabel('Products/month')
    plt.xticks(x)
    plt.grid()
    plt.show()

def mean_product(data):
    sumarr = np.empty(0)

    for i in range(len(data)):
        mean = round(np.mean(data[i]))
        sum = np.sum(data[i])
        sumarr = np.append(sumarr, sum)
        print(f"The mean products produced from company nbr {i} is {mean} product")
    
    # calculating the total mean 
    arr = np.empty(0)
    nbr_workers_per_company = np.empty(0) 

    for i in range(len(data)):
        for j in range(len(data[i])):
            arr = np.append(arr, data[i][j])
        nbr_workers_per_company = np.append(nbr_workers_per_company, j)
    

    mean = round(np.mean(arr)) 
    print(f"The mean products produced from all the companies is {mean} per worker")
    yield arr
    yield nbr_workers_per_company
    yield sumarr 

def ploteverything(arr):
    x = np.arange(len(arr))
    plt.plot(x, arr, marker='o')
    plt.xlabel("Rank of workers")
    plt.ylabel("Porudcts/month")
    plt.grid()
    plt.show()

def products_terms_workers(sumarr, nbrworkers):
    arr2d = np.column_stack((nbrworkers, sumarr))
    sortedindex = np.argsort(arr2d[:, 0])

    arr2d = arr2d[sortedindex] 

    print(arr2d)

    # plotting
    plt.plot(arr2d[: , 0] , arr2d[: , 1] , marker = 'o')
    plt.xlabel('nbr workers per company')
    plt.ylabel("Products/ month")
    plt.grid()
    plt.show()

def main():
    data_frame = file_handling()
    gen = mean_product(data_frame)
    arr = next(gen)
    nbrworkers = next(gen)
    sumarr = next(gen)  
    products_terms_workers(sumarr, nbrworkers)


main()