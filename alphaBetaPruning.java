
/* Taken from my Gomoku Ai's alpha beta pruning addition. Acts as a Pseudocode for understanding.
Your implementation will be differnet for your use while it retains the core algorithn. 
@author unobatbayar
*/
class alphaBetaPruning{
    public int[] minimax(Color[][] board, int depth, Color player, int alpha, int beta, Color me, Color enemy) {

        Color[][] new_board = new Color[8][8];
		for (int i = 0;i < 8;i++){
			for (int j = 0;j < 8;j++){
				new_board[i][j] = board[i][j];
			}
        }
        if(depth == 0 || empty(new_board) != true){
            int value = utility(board, player, me);
            int [] utility_value = {0,0, value};
            return utility_value;
        }

        int[] minimax = {0,0,0};

        //Available moves
		for(int row = 0; row <8; row++){
            for(int col = 0; col < 8; col++){
                if(new_board[row][col] == null){

                    new_board[row][col] = player;
                    if(player == me){
                        minimax[1] = -1000000;
                        int[] child = minimax(board, depth-1, enemy, alpha, beta, me, enemy);
                        new_board[row][col] = null;
                        if (child[1] > minimax[1]) {
                            minimax[0] = move; 
                            minimax[1] = child[2]; 
                        }
                        minimax[2] = Math.max(child[2], minimax[2]);
                        alpha = Math.max(alpha, minimax[2]);
                        if(beta <= alpha){
                            break;
                        }
                    }
                    else if(player == enemy){
                        minimax[1] = 1000000;
                        int[] child = minimax(board, depth-1, me, alpha, beta, me, enemy);
                        new_board[row][col] = null;
                        if (child[1] < minimax[1]) {
                            minimax[0] = move; 
                            minimax[1] = child[1]; 
                        }
                        minimax[1] = Math.min(child[1], minimax[1]);
                        beta = Math.min(beta, minimax[1]);
                        if (beta <= alpha){
                            break;
                        }  	
                    }
                }
            }
        }
        return minimax;
    }

}