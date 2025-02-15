import java.util.Arrays;

public class SortRunner {
    public static void main(String[] args) {
        String algo = args[0];
        int[] arr = Arrays.stream(args[1].split(",")).mapToInt(Integer::parseInt).toArray();

        if (algo.equals("BubbleSort")) {
            Algorithms.bubbleSort(arr);
        } else if (algo.equals("QuickSort")) {
            Algorithms.quickSort(arr, 0, arr.length - 1);
            System.out.println("Sorted: " + Arrays.toString(arr));
        }
    }
}
