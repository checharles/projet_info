from graph import catalog_from_file
from trajet_truck import cost_traject
data_path = "/home/onyxia/projet_info/"
c = catalog_from_file(data_path + "input/trucks.2.in")
print(len(c))


print(cost_traject(3,2))