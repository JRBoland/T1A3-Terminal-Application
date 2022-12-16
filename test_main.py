from functions import view_dogs, fed_dog_count_hero_banner, return_to_main, fed_dog_counter, new_dog_menu, add_new_dog

items = view_dogs()

def test_view_dogs_length_list():
    items = view_dogs()
    assert len(items) == 10

def test_add_item_last_element():
    add_new_dog(items, "Scooby", "Yes")
    assert items[-1]["Name"] == "Scooby"