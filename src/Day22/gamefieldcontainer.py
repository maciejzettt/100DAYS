from gamecomponent import GameFieldComponent
from turtle import Screen
from typing import TypeVar, Type
from gameover import GameOver


GFC = TypeVar('GFC', bound=GameFieldComponent)


class GameFieldContainer:

    def __init__(self, field_height: int, field_width: int, window_title: str):
        self.screen = Screen()
        self.screen.setup(width=field_width, height=field_height)
        self.screen.title(window_title)
        self.screen.bgcolor('black')
        self.screen.tracer(n=0)
        self.screen.listen()
        self._components = list[dict]()
        self._is_valid = True

    def register_component(self, name: str, component_class: Type[GameFieldComponent], **component_init_kwargs):
        if not issubclass(component_class, GameFieldComponent):
            raise TypeError(f"register_component: A component must be a subclass of GameFieldComponent")
        if name in [c['name'] for c in self._components]:
            raise NameError(f"register_component: A component of this name has already been registered: {name}.")
        self._components.append({'name': name, 'class': component_class, 'args': component_init_kwargs})

    def components_init(self):
        for component in self._components:
            if 'instance' in component.keys():
                print(f"\tInitializing component '{component['name']}' skipped. Already initialized.")
            else:
                component_args = component['args']
                if len(component_args) == 0:
                    print(f"\tInitializing component '{component['name']}': {component['class']} without arguments.")
                    component['instance'] = component['class'](self.screen)
                elif len(component_args) > 0:
                    print(f"\tInitializing component '{component['name']}': {component['class']} with arguments: {component_args}.")
                    component['instance'] = component['class'](self.screen, **component_args)
                else:
                    raise Exception("components_init has reached invalid state: number of arguments seems negative.")

    def step_through_components(self):
        for component in self._components:
            if 'instance' in component.keys():
                try:
                    component['instance'].step()
                except GameOver:
                    self._is_valid = False
                    return
            else:
                raise ReferenceError(f"step_through_components: Component'{component['name']}' has not been initialized.")
            self.update_screen()

    def get_component_by_name(self, component_name: str) -> GFC:
        for component in self._components:
            if component['name'] == component_name:
                try:
                    return component['instance']
                except KeyError:
                    raise KeyError(f"get_component_by_name: Component '{component_name}' has not been initialized.")
        raise NameError(f"get_component_by_name: Component '{component_name}' not found.")

    def register_action(self, component_name: str, key_binding: str, method_name: str):
        component = self.get_component_by_name(component_name)
        if hasattr(component, method_name):
            method = getattr(component, method_name)
            if callable(method):
                self.screen.onkey(method, key_binding)
                print(f"\tRegistered action '{method_name}':{method} for component '{component_name}' on key '{key_binding}'.")
            else:
                AttributeError(f"register_action: Attribute '{method_name}' of component '{component_name}' is not callable.")
        else:
            raise AttributeError(f"register_action: Component '{component_name}' has no attribute '{method_name}'")

    def update_screen(self):
        self.screen.update()

    def is_valid(self) -> bool:
        return self._is_valid
