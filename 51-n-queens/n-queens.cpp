class Solution {
public:
    bool isValid(int row, int col, vector<string>&A,int n){
        int tempr = row, tempc = col;

        while(tempr >= 0){
            if(A[tempr][col] == 'Q') return false;
            tempr--;
        }
        tempr = row;
        while(tempr >= 0 && tempc < n){
            if(A[tempr][tempc] == 'Q') return false;
            tempr--;
            tempc++;
        }
        tempr = row, tempc = col;
        while(tempr >= 0 && tempc >= 0){
            if(A[tempr][tempc] == 'Q') return false;
            tempr--;
            tempc--;
        }
        return true;
    }

    void solve(int row, vector<vector<string>>&ds, vector<string>&A, int n){
        if (row == n){
            ds.push_back(A);
            return;
        }
        for(int col = 0; col < n; col++){
            if(isValid(row,col,A,n)){
                A[row][col] = 'Q';
                solve(row + 1,ds,A,n);
                A[row][col] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>>ds;
        vector<string>A;
        for(int i = 0; i < n; i++){
            string s;
            for(int j = 0; j < n; j++){
                s += '.';
            }
            A.push_back(s);
        }

        solve(0,ds,A,n);
        return ds;
    }
};