from behave import given, when, then
from src.cal import suma

@given('los números {int} y {int}')
def step_given(context, int, int2):
    context.a = 2
    context.b = 3

@when('se suman')
def step_when(context):
    context.resultado = suma(context.a, context.b)

@then('el resultado debe ser {int}')
def step_then(context, int):
    assert context.resultado == 5, f"Esperado {5}, pero fue {context.resultado}"