import string
import random


class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        first_section = id[:2]
        second_section = ''.join(random.choices(string.digits, k=2))
        third_section = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{first_section}-{second_section}-{third_section}"
    
    
    def generate_vehicle_value(self, brand):
        # gerar o preco do veiculo
        catalogue_price = 0
        if brand == 'Tesla Model 3':
            catalogue_price = 445000
        elif brand == 'Chevrolet Bold':
            catalogue_price = 317000
        elif brand == 'BMW i3':
            catalogue_price = 319950
        elif 'Honda Civic LX':
            catalogue_price = 127900

        return catalogue_price



    def generate_vehicle_tax(self, vehicle):

        electric_models = [
            'Tesla Model 3','Chevrolet Bold', 'BMW i3'
        ]

        # calcula a taxa de imposto. o padrão é 5%. para carros eletréticos o valor é 2%
        tax_percentage = 0.05
        
        if vehicle in electric_models:
            tax_percentage = 0.02

        # calcula a valor a ser pago
        payable_tax = tax_percentage * self.generate_vehicle_value(vehicle)

        return payable_tax



class Application:

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()

        # gera um id com 12 caracteres
        vehicle_id = registry.generate_vehicle_id(12)

        # gera a placa de baseado no id do veículo
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # gera a taxa que será paga pelo veículo
        payable_tax = registry.generate_vehicle_tax(brand)
        
        # calcula o preço total com imposto
        total = registry.generate_vehicle_value(brand) + payable_tax

        print(f'Marca: {brand}')
        print(f'ID: {vehicle_id}')
        print(f'Placa: {license_plate}')
        print(f'Imposto a ser pago: {payable_tax}')
        print(f'Preço Total: {total}')


app = Application()
app.register_vehicle('Tesla Model 3')
