

class BitwiseLogicGate:

    def __init__(self):
        self.data = []
        self.assignment_data = []
        self.connection_data = []
        self.NOT_data = []
        self.converted_data = []
        self.unhandled_data = []
        self.variables = []

    def read_input_file(self, filename: str):
        with open(filename) as file:
            self.data = file.readlines()

    def convert_data(self):
        for instruction in self.data:
            split_instruction = instruction.split()

            if len(split_instruction) == 3:
                self.assignment_data.append({
                    "type": 'assignment',
                    "in_val": split_instruction[0],
                    "out_val": split_instruction[2],
                })
            elif len(split_instruction) == 4:
                self.NOT_data.append({
                    "type": 'NOT',
                    "operator": split_instruction[0],
                    "in_val": split_instruction[1],
                    "out_val": split_instruction[3],
                })
            elif len(split_instruction) == 5:
                self.connection_data.append({
                    "type": 'connection',
                    "operator": split_instruction[1],
                    "in_val": split_instruction[0],
                    "in_val2": split_instruction[2],
                    "out_val": split_instruction[4],
                })
            else:
                self.unhandled_data.append(split_instruction)

        self.converted_data = self.assignment_data + self.NOT_data + self.connection_data

    def build_logic_gate(self):

        while self.converted_data:
            print(f"entries left: {len(self.converted_data)}")
            for instruction in self.converted_data[:]:
                self.handle_assignment(instruction)

                try:
                    self.handle_not(instruction)
                    self.handle_or(instruction)
                    self.handle_and(instruction)
                    self.handle_lshift(instruction)
                    self.handle_rshift(instruction)

                except KeyError:
                    pass

            self.update_instruction_list()

    def update_instruction_list(self):
        for var in self.variables:
            for idx, instruction in enumerate(self.converted_data[:]):

                if var['name'] == instruction['in_val']:
                    instruction['in_val'] = var['val']
                    self.converted_data[idx] = instruction
                try:
                    if var['name'] == instruction['in_val2']:
                        instruction['in_val2'] = var['val']
                        self.converted_data[idx] = instruction
                except KeyError:
                    pass

    def handle_assignment(self, instruction):
        try:
            if instruction['type'] == 'assignment':
                try:
                    output = instruction["in_val"]
                    int(output)
                    self.variables.append({
                        'name': str(instruction['out_val']),
                        'val': output
                    })
                    self.converted_data.remove(instruction)

                except ValueError:
                    pass
        except KeyError:
            pass

    def handle_not(self, instruction):
        if instruction['operator'] == 'NOT':
            try:
                output = str(~int(instruction['in_val']))
                # assume for now that instructions are good --> no check for existance needed --> not finnished yet
                self.variables.append({
                    'name': str(instruction['out_val']),
                    'val': output
                })
                self.converted_data.remove(instruction)

            except ValueError:
                pass

    def handle_or(self, instruction):
        if instruction['operator'] == 'OR':
            try:
                output = str(int(instruction['in_val']) | int(instruction['in_val2']))
                self.variables.append({
                    'name': str(instruction['out_val']),
                    'val': output
                })
                self.converted_data.remove(instruction)

            except ValueError:
                pass

    def handle_and(self, instruction):
        if instruction['operator'] == 'AND':
            try:
                output = str(int(instruction['in_val']) & int(instruction['in_val2']))
                self.variables.append({
                    'name': str(instruction['out_val']),
                    'val': output
                })
                self.converted_data.remove(instruction)

            except ValueError:
                pass

    def handle_lshift(self, instruction):
        if instruction['operator'] == 'LSHIFT':
            try:
                output = str(int(instruction['in_val']) << int(instruction['in_val2']))
                self.variables.append({
                    'name': str(instruction['out_val']),
                    'val': output
                })
                self.converted_data.remove(instruction)

            except ValueError:
                pass

    def handle_rshift(self, instruction):
        if instruction['operator'] == 'RSHIFT':
            try:
                output = str(int(instruction['in_val']) >> int(instruction['in_val2']))
                self.variables.append({
                    'name': str(instruction['out_val']),
                    'val': output
                })
                self.converted_data.remove(instruction)

            except ValueError:
                pass
