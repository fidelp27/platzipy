import matplotlib.pyplot as plt

def generate_pie_chart():
    labels =["A", "B", "C"]
    values = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels);
    #plt.show()=> para que muestre la gráfica y detenga el archivo
    #=> para guardar el archivo como una imagen 
    plt.savefig("pie.png")
    plt.close()
    
     