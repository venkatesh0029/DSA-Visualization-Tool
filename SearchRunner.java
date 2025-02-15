import java.util.Arrays;

public class SearchRunner {
    public static void main(String[] args) {
        String algo = args[0];
        int target = Integer.parseInt(args[2]);
        int[] arr = Arrays.stream(args[1].split(",")).mapToInt(Integer::parseInt).toArray();

        int result = -1;
        if (algo.equals("BinarySearch")) {
            Arrays.sort(arr);
            result = Algorithms.binarySearch(arr, target);
        } else if (algo.equals("LinearSearch")) {
            result = Algorithms.linearSearch(arr, target);
        }

        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found.");
        }
    }
}
