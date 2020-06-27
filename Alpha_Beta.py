##########################
# EASHAN SAPRE
# 2017A3PS1158P
##########################

import copy

class State(object):
	""" State """
	def __init__(self, matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], player = 1):
		self.matrix = matrix
		self.player = player

	def __str__(self):
		if self.player == 1:
			return str(self.matrix[0]) + "\n" + str(self.matrix[1]) + "\n" + str(self.matrix[2]) + "\n" + str(self.matrix[3]) + "\n Bot's Turn"
		else:
			return str(self.matrix[0]) + "\n" + str(self.matrix[1]) + "\n" + str(self.matrix[2]) + "\n" + str(self.matrix[3]) + "\n Player's Turn"

	def __repr__(self):
		return str(self.matrix)

	def __hash__(self):
		return hash(tuple([tuple(x) for x in self.matrix]))

	def count_coins(self, player_num):
		count = 0
		if player_num == 1:
			for i in self.matrix:
				for j in i:
					if j == 1:
						count += 1
		else:
			for i in self.matrix:
				for j in i:
					if j == 2:
						count += 1
		return count

	def player_turn(self):
		bot_coins = self.count_coins(1)
		human_coins = self.count_coins(2)
		if bot_coins == human_coins:
			return 1
		else:
			return 2

	def change_player(self):
		if self.player == 1:
			return 2
		else:
			return 1

	def action(self):
		action_list = ['x', 'x', 'x', 'x']
		if self.matrix[3][0] == 0:
			action_list[0] = 0
		if self.matrix[3][1] == 0:
			action_list[1] = 1
		if self.matrix[3][2] == 0:
			action_list[2] = 2
		if self.matrix[3][3] == 0:
			action_list[3] = 3
		return action_list

	def lowest_empty_row(self, col):
		if self.matrix[0][col] == 0:
			return 0
		elif self.matrix[1][col] == 0:
			return 1
		elif self.matrix[2][col] == 0:
			return 2
		elif self.matrix[3][col] == 0:
			return 3
		else:
			return -1

	def Successor_function(self, action):
		if action != 'x':
			row = self.lowest_empty_row(action)
			temp = copy.deepcopy(self.matrix)
			temp[row][action] = self.player_turn()
            # below changing matrix and self player value
			new_state = State(matrix = temp, player = self.change_player())
			return new_state

	def check_verti(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and row_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num]:
			return True
		else:
			return False

	def check_hori(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and col_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num][col_num + 1] and self.matrix[row_num][col_num] == self.matrix[row_num][col_num + 2]:
			return True
		else:
			return False

	def check_right_diag(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and row_num <= 1 and col_num <= 1 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num + 1] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num + 2]:
			return True
		else:
			return False

	def check_left_diag(self, row_num, col_num):
		if self.matrix[row_num][col_num] != 0 and row_num <= 1 and col_num >= 2 and self.matrix[row_num][col_num] == self.matrix[row_num + 1][col_num - 1] and self.matrix[row_num][col_num] == self.matrix[row_num + 2][col_num - 2]:
			return True
		else:
			return False
	
	def check_full(self):
		for ele in self.matrix[3]:
			if ele == 0:
				return False
		return True

	def terminal_test(self):
		is_full = False
		is_won = False
		for row_num, row in enumerate(self.matrix):
			for col_num, element in enumerate(row):
				result = self.check_hori(row_num, col_num)
				if result == True:
					
					is_won = True
					
				result = self.check_verti(row_num, col_num)
				if result == True:
					
					is_won = True
					
				result = self.check_right_diag(row_num, col_num)
				if result == True:
					
					is_won = True
					
				result = self.check_left_diag(row_num, col_num)
				if result == True:
					
					is_won = True
					
				result = self.check_full()
				if result == True:
					
					is_full = True
					
		
		return is_full, is_won

	def utility_value(self):
		if self.check_full():
			return 0
		else:
			if self.player_turn() == 1:
				return -1
			else:
				return 1

	def alpha_beta_search(self):
		v, action, num_nodes = max_value(self, -100, 100)
		return action, num_nodes
		
def min_value(state, alpha, beta):
	
	is_full, is_won = state.terminal_test()
	if is_won:
		return state.utility_value(), None, 0
	elif is_full:
		return 0, None, 0

	num_nodes = 0
	v = 100
	action_list = state.action()
	ret = None

	for action in action_list:
		temp = state.Successor_function(action)
		if temp is not None:
			
			num_nodes += 1
			
			maxi, garb, temp_num_nodes = max_value(temp, alpha, beta)
			num_nodes += temp_num_nodes
			
			if v > maxi:
				v = maxi
				ret = action
			
			if v <= alpha:
				return v, ret, num_nodes
            
			beta = min(beta, v)
			
			if alpha >= beta:
			    break
	
	return v, ret, num_nodes


def max_value(state, alpha, beta):
	
	is_full, is_won = state.terminal_test()
	if is_won:
		return state.utility_value(), None, 0
	elif is_full:
		return 0, None, 0

	num_nodes = 0
	v = -100
	action_list = state.action()
	ret = None

	for action in action_list:
		temp = state.Successor_function(action)
		if temp is not None:
			num_nodes += 1
			mini, garb, temp_num_nodes = min_value(temp, alpha, beta)
			num_nodes += temp_num_nodes
			
			if v < mini:
				
				v = mini
				ret = action
			
			if v >= beta:
				return v, ret, num_nodes
			
			alpha = max(alpha, v)
			if alpha >= beta:
				break
	
	return v, ret, num_nodes

def start_game_alpha_beta():
	begin = State()
	state = begin
	while True:
		bot_action = state.alpha_beta_search()
		next_state = state.Successor_function(bot_action)
		print(next_state)
		is_full, is_won = next_state.terminal_test()
		if is_won == True:
			print("BOT WINS")
			break
		elif is_full == True:
			print("DRAW")
			break
		human_action = input()
		human_action = int(human_action)
		state = next_state.Successor_function(human_action)
		print(state)
		is_full, is_won = next_state.terminal_test()
		if is_won == True:
			print("HUMAN WINS")
			break
		elif is_full == True:
			print("DRAW")
			break


	
if __name__ == "__main__":
	start_game_alpha_beta()
