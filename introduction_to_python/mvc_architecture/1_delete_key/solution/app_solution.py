import model_solution as model
import view_solution as view

old_list = model.get_list()
print(view.display(old_list))

to_del = input(view.delete_key())
model.del_list_key(to_del)

final_list = model.get_list()

print(view.display(final_list))