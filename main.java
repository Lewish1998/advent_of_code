import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

class Scratch {
    static Map<String, Integer> numbers = Map.of("one", 1, "two", 2, "three", 3, "four", 4, "five", 5, "six", 6, "seven", 7, "eight", 8, "nine", 9);

    public static void main(String[] args) {
        BufferedReader reader;
        try {
//            reader = new BufferedReader(new FileReader("/Users/ghalstea/Library/Application Support/JetBrains/IntelliJIdea2023.2/scratches/2023/Day1/test.input.2.txt"));
            reader = new BufferedReader(new FileReader("/Users/lewis/Desktop/Projects/advent_of_code/day_1.txt"));
            String line = reader.readLine();
            int total = 0;
            while (line != null) {
                String leftMostDigit = getLeftMostDigit(line);
                String rightMostDigit = getRightMostDigit(line);
                total += Integer.parseInt(leftMostDigit + rightMostDigit);

                line = reader.readLine();
            }
            reader.close();
            System.out.println(total);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static String getLeftMostDigit(String line) {
        StringBuilder buildingFromTheLeft = new StringBuilder();
        for(int x = 0; x < line.length(); x++) {
            String currentChar = line.substring(x, x + 1);
            if (currentChar.matches("[0-9]")) {
                return currentChar;
            } else {
                buildingFromTheLeft.append(currentChar);
                String number = getNumber(buildingFromTheLeft.toString());
                if(number != null) {
                    return number;
                }
            }
        }
        return null;
    }

    public static String getRightMostDigit(String line) {
        StringBuilder buildingFromTheRight = new StringBuilder();
        for(int x = line.length() -1; x>=0; x--) {
            String currentChar = line.substring(x, x + 1);
            if (currentChar.matches("[0-9]")) {
                return currentChar;
            } else {
                buildingFromTheRight.insert(0,currentChar);
                String number = getNumber(buildingFromTheRight.toString());
                if(number != null) {
                    return number;
                }
            }
        }
        return null;
    }

    public static String getNumber(String text) {
        for (Map.Entry<String, Integer> entry : numbers.entrySet()) {
            if (text.contains(entry.getKey())) {
                return entry.getValue().toString();
            }
        }
        return null;
    }

}