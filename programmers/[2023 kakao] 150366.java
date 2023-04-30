// https://school.programmers.co.kr/learn/courses/30/lessons/150366

package programmers;

import java.util.*;

class Solution {
    private String[][] table;
    private int[] parent;
    private List<String> answerList;
    private int pSize = 51*51 + 1;
    
    public String[] solution(String[] commands) {
        final String UPDATE = "UPDATE";
        final String MERGE = "MERGE";
        final String UNMERGE = "UNMERGE";
        final String PRINT = "PRINT";
        final String EMPTY = "EMPTY";
        
        answerList = new ArrayList<>();
        
        parent = new int[pSize];
        table = new String[51][51];
        
        for(int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }
        
        for(int k = 0; k < commands.length; k++) {
            String[] parsed_command = commands[k].split(" ");

            /* UPDATE */
            if(parsed_command[0].equals(UPDATE)) {
                if(parsed_command.length == 3) {
                    String value1 = parsed_command[1];
                    String value2 = parsed_command[2];
                    if(value1.equals(value2)) continue;
                    changeValue(value1, value2);
                } else {
                    int r = Integer.parseInt(parsed_command[1]);
                    int c = Integer.parseInt(parsed_command[2]);
                    String value = parsed_command[3];
                    
                    int np = find(pton(r, c));
                    table[ntor(np)][ntoc(np)] = value;
                }
            /* MERGE */
            } else if(parsed_command[0].equals(MERGE)) {
                int r1 = Integer.parseInt(parsed_command[1]);
                int c1 = Integer.parseInt(parsed_command[2]);
                int r2 = Integer.parseInt(parsed_command[3]);
                int c2 = Integer.parseInt(parsed_command[4]);

                int np1 = find(pton(r1, c1));
                int np2 = find(pton(r2, c2));

                // 이미 같은 셀인 경우 병합 안함
                if(np1 == np2) continue;

                // 두 셀을 합치고, 부모셀에 value 넣기
                union(np1, np2);
                int np = find(np1);

                r1 = ntor(np1);
                c1 = ntoc(np1);
                r2 = ntor(np2);
                c2 = ntoc(np2);

                String value = table[r1][c1]==null ? table[r2][c2] : table[r1][c1];

                table[r1][c1] = null;
                table[r2][c2] = null;
                table[ntor(np)][ntoc(np)] = value;
            /* UNMERGE */
            } else if(parsed_command[0].equals(UNMERGE)) {
                int r = Integer.parseInt(parsed_command[1]);
                int c = Integer.parseInt(parsed_command[2]);
                int np = find(pton(r, c));

                int pr = ntor(np);
                int pc = ntoc(np);
                String value = table[pr][pc];
                
                // 큰 수가 부모가 되도록 union했기 때문에
                // 1. 작은 수 부터 초기화 해도 부모 노드 못찾아 갈 일 없음  (작은 수가 큰 수의 부모인 경우 없음)
                // 2. 전체가 아닌, np까지만 초기화 가능
                for(int i = 0; i <= np; i++) {
                    if(find(i) == np) {
                        parent[i] = i;
                        table[ntor(i)][ntoc(i)] = null;
                    }
                }
                table[r][c] = value;
            /* PRINT */
            } else if(parsed_command[0].equals(PRINT)) {
                int r = Integer.parseInt(parsed_command[1]);
                int c = Integer.parseInt(parsed_command[2]);
                int n = find(pton(r, c));
                String value = table[ntor(n)][ntoc(n)];
                if(value == null) value = EMPTY;
                answerList.add(value);
            }
        }
        return answerList.toArray(new String[answerList.size()]);
    }
    
    public void union(int point1, int point2) {
        point1 = find(point1);
        point2 = find(point2);
        
        if(point1 == point2) return;
        if(point1 > point2) parent[point2] = point1;
        else parent[point1] = point2;
    }
    
    public int find(int point) {
        if(parent[point] == point) {
            return point;
        }
        parent[point] = find(parent[point]);
        return parent[point];
    }
    
    public int pton(int r, int c) {
        return r*51+c;
    }
    
    public int ntor(int n) {
        return n/51;
    }
    
    public int ntoc(int n) {
        return n%51;
    }
    
    public void changeValue(String from, String to) {
        for(int i = 0; i < table.length; i++) {
            for(int j = 0; j < table[i].length; j++) {
                if(table[i][j] == null) continue;
                if(table[i][j].equals(from)) {
                    table[i][j] = to;
                }
            }
        }
    }
}