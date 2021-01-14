import model_solution as model 
import view_solution as view 

model.create()
result = model.query()
data = view.display(result)
print(data)