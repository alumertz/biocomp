#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int needleman_wunsch(string seq1, string seq2, int match=1, int mismatch=-1, int gap=-2) {
    // Initialize the matrix with zeros
    int rows = seq1.size();
    int cols = seq2.size();
    vector<vector<int>> matrix(rows, vector<int>(cols, 0));

    // Initialize the first row and column
    for (int i = 1; i < rows; i++) {
        matrix[i][0] = i * gap;
    }
    for (int j = 1; j < cols; j++) {
        matrix[0][j] = j * gap;
    }
    

    // Fill the matrix
    for (int i = 1; i < rows; i++) {
        for (int j = 1; j < cols; j++) {
            int score;
            if (seq1[i-1] == seq2[j-1]) {
                score = match;
            } else {
                score = mismatch;
            }
            matrix[i][j] = max({matrix[i-1][j-1] + score,
                                matrix[i-1][j] + gap,
                                matrix[i][j-1] + gap});
        }
    }

    int score = matrix[rows-1][cols-1];
    return score;
}

string readFile2(const string &fileName)
{
    ifstream ifs(fileName.c_str(), ios::in | ios::binary | ios::ate);

    ifstream::pos_type fileSize = ifs.tellg();
    ifs.seekg(0, ios::beg);

    vector<char> bytes(fileSize);
    ifs.read(bytes.data(), fileSize);

    return string(bytes.data(), fileSize);
}

int main(){

    string numseq1,numseq2;

    cin >> numseq1;
    cin >> numseq2;
    
    
    
    //string seq1 = readFile2("seq/seq.txt");
    //string seq2 = readFile2("seq/seq2.txt");
    string arq1 = readFile2("seq/seq_"+numseq1+".txt");
    string arq2 = readFile2("seq/seq_"+numseq2+".txt");

    seq[1] = 

    cout << "leu";
    int score = needleman_wunsch(seq1,seq2,1,-1,-2);

    cout << " fim " << score;

    
    return 0;
}