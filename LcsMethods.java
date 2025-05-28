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

    private static void backtrack(Integer[][] dpm, String string1, String string2, Integer indexString1, Integer indexString2, Integer lcsLen, String current, Set<String> result){
        if (indexString1 == 0 || indexString2 == 0){
            if (current.length() == lcsLen && isSubsequence(current, string2))
                result.add(current);
            return;
        }
        if (string1.charAt(indexString1-1) == string2.charAt(indexString2-1))
            backtrack(dpm, string1, string2, indexString1-1, indexString2-1, lcsLen, string1.charAt(indexString1-1) + current, result);
        else{
            if (dpm[indexString1-1][indexString2] > dpm[indexString1][indexString2-1])
                backtrack(dpm, string1, string2, indexString1-1, indexString2, lcsLen, current, result);
            else if (dpm[indexString1][indexString2-1] > dpm[indexString1-1][indexString2])
                backtrack(dpm, string1, string2, indexString1, indexString2-1, lcsLen, current, result);
            else {
                backtrack(dpm, string1, string2, indexString1-1, indexString2, lcsLen, current, result);
                backtrack(dpm, string1, string2, indexString1, indexString2-1, lcsLen, current, result);
            }
        }
    }
}
