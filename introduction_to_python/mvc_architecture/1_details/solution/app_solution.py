import model_solution as model 
import view_solution as view 

name = input(view.capture_name())
age = input(view.capture_age())
result = [name, age]
model.store(result)

info = view.display(result)
print(info)