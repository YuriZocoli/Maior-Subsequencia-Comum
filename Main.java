import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Insira a quantidade de dados a ser inserido:");
        var numberOfData = scanner.nextInt();
        for(Integer i = 0; i < numberOfData; i++){
            scanner.nextLine();
            System.out.println("Insira os dados 1:");
            var string1 = scanner.nextLine();
            System.out.println("Insira os dados 2:");
            var string2 = scanner.nextLine();
            var dpm = LcsMethods.getDinamicProgramingMatrix(string1, string2);
            var result = LcsMethods.getAllLcs(string1, string2, dpm);
            if (result.size() > 0){
                System.out.println("Resultados sequencia "+(i+1)+":");
                for(String lcs : result.stream().sorted().toList()){
                    System.out.println(lcs);
                }
            }
            else{
                System.out.println("Sem Lcs");
            }
            if (i < numberOfData -1)
                System.out.println();
        }
        scanner.close();
    }
}