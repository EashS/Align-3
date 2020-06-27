##########################
# EASHAN SAPRE
# 2017A3PS1158P
##########################


from Setup_GUI import *
from Event_Handler import *
from turtle import *
from MinMax import *
from Alpha_Beta import *
from time import sleep, time
import config

def main():
    
	screen, r_cood_list, gameplay_cood_list, grid_square_size, grid_start_coordinates, text_t, grid_t = initialise_board()
	fill_t = Turtle()
	fill_t.speed(0)
	
	config.init()
	begin = myState()
	t0 = time()
	bot_action, temp_num_nodes, depth_of_stack = begin.minimax_decision()
	t1 = time()

	counter = 0
	counter = fillCircles(grid_start_coordinates, grid_square_size, 1, fill_t, [0, bot_action])
	
	update()
	next_state = begin.Successor_function(bot_action)
	text_t.penup()
	text_t.setpos(r_cood_list[1][0], r_cood_list[1][1])
	text_t.write(str(sys.getsizeof(myState())) + "Bytes", font = ("Arial", 15, "normal"))

	text_t.setpos(r_cood_list[2][0], r_cood_list[2][1])
	text_t.write(str(depth_of_stack), font = ("Arial", 15, "normal"))

	click_action = CheckClick(gameplay_cood_list, grid_start_coordinates, grid_square_size, screen, grid_t, text_t, fill_t, r_cood_list, next_state, temp_num_nodes)
	click_action.tot_time_minimax += t1 - t0
	
	if config.fillcircle_counter != 0 and config.newgame_flag == 0:
		screen.onclick(click_action.onclick_action)
        
	screen.listen()
		
	done()
    
if __name__ == "__main__":
	main()