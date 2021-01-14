import model_solution as model 
import view_solution as view 

fruits = model.get_store()

# new_fruit = input(view.ask_fruit())
# model.add_fruits(new_fruit)

remove_fruit = input(view.ask_fruit())
model.update_fruits(remove_fruit)

show = view.show_fruits()
print(show)