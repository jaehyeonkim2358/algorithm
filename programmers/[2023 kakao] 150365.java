// https://school.programmers.co.kr/learn/courses/30/lessons/150365

package programmers;

class Solution {
    private Move[] moves = {Move.DOWN, Move.LEFT, Move.RIGHT, Move.UP};
    private int N, M, K, R, C;
    private String answer;

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        N = n; M = m; K = k; R = r; C = c;
        answer = null;
        StringBuilder sb = new StringBuilder();
        dfs(x, y, sb, 0);
        if(answer == null) return "impossible";
        return answer;
    }

    public void dfs(int row, int col, StringBuilder sb, int depth) {
        if(depth > K || answer != null) return;
        if(depth == K) {
            if(row == R && col == C) {
                answer = sb.toString();
            }
            return;
        }

        for(int i = 0; i < moves.length; i++) {
            int newRow = row + moves[i].move[0];
            int newCol = col + moves[i].move[1];
            if(check(newRow, newCol, depth)) {
                sb.append(moves[i].name);
                dfs(newRow, newCol, sb, depth+1);
                sb.setLength(sb.length()-1);
            }
        }
    }

    public boolean check(int x, int y, int count) {
        if(x < 1 || x > N) return false;
        if(y < 1 || y > M) return false;
        if((Math.abs(x-R) + Math.abs(y-C))%2 != (K-count-1)%2) return false;
        if((Math.abs(x-R) + Math.abs(y-C)) > K-count) return false;
        return true;
    }

    enum Move {
        UP('u', new int[]{-1, 0}),
        DOWN('d', new int[]{1, 0}),
        LEFT('l', new int[]{0, -1}),
        RIGHT('r', new int[]{0, 1});
    
        private final char name;
        private final int[] move;
    
        Move(char name, int[] move) {
            this.name = name;
            this.move = move;
        }
    }
}