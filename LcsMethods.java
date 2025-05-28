import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class LcsMethods {
    
    public static Integer[][] getDinamicProgramingMatrix(String string1, String string2){
        var lenString1 = string1.length();
        var lenString2 = string2.length();
        var dpm = new Integer[lenString1+1][lenString2+1];

        for(Integer i = 0; i < lenString1+1; i++){
            for(Integer j = 0; j < lenString2+1; j++){
                dpm[i][j] = 0;
            }
        }
        for(Integer i = 1; i < lenString1+1; i++){
            for(Integer j = 1; j < lenString2+1; j++){
                if(string1.charAt(i-1) == string2.charAt(j-1))
                    dpm[i][j] = dpm[i-1][j-1] + 1;
                else
                    dpm[i][j] = Math.max(dpm[i-1][j], dpm[i][j-1]);
            }
        }
        return dpm;
    }

    public static boolean isSubsequence(String sub, String string) {
        if (sub.isEmpty())
            return true;
        
        int subIndex = 0;
        for (int i = 0; i < string.length() && subIndex < sub.length(); i++) {
            if (sub.charAt(subIndex) == string.charAt(i)) {
                subIndex++;
            }
        }
        return subIndex == sub.length();
    }

    public static Set<String> getAllLcs(String string1, String string2, Integer[][] dpm){
        Set<String> result = new HashSet<String>();
        var lcsLen = dpm[string1.length()][string2.length()];
        backtrack(dpm, string1, string2, string1.length(), string2.length(), lcsLen, "", result);
        return result;
    }

    private static void backtrack(Integer[][] dp, String s1, String s2, Integer i, Integer j, Integer lcs_len, String current, Set<String> resultado){
        if (i == 0 || j == 0){
            if (current.length() == lcs_len && isSubsequence(current, s2))
                resultado.add(current);
            return;
        }
        if (s1.charAt(i-1) == s2.charAt(j-1))
            backtrack(dp, s1, s2, i-1, j-1, lcs_len, s1.charAt(i-1) + current, resultado);
        else{
            if (dp[i-1][j] > dp[i][j-1])
                backtrack(dp, s1, s2, i-1, j, lcs_len, current, resultado);
            else if (dp[i][j-1] > dp[i-1][j])
                backtrack(dp, s1, s2, i, j-1, lcs_len, current, resultado);
            else {
                backtrack(dp, s1, s2, i-1, j, lcs_len, current, resultado);
                backtrack(dp, s1, s2, i, j-1, lcs_len, current, resultado);
            }
        }
    }
}
