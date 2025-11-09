//display a binary number into other number systems
public class Binary7{
    public static void main(String[] args) {
        int binaryNumber = 1011; // Example binary number
        int decimalNumber = 0;
        int octalNumber = 0;

        // Convert binary to decimal
        int power = 0;
        int tempBinary = binaryNumber;
        while (tempBinary > 0) {
            int lastDigit = tempBinary % 10;
            decimalNumber += lastDigit * Math.pow(2, power);
            power++;
            tempBinary /= 10;
        }

        // Convert decimal to octal
        int tempDecimal = decimalNumber;
        int octalPlace = 1;
        while (tempDecimal > 0) {
            int remainder = tempDecimal % 8;
            octalNumber += remainder * octalPlace;
            octalPlace *= 10;
            tempDecimal /= 8;
        }

        // Convert decimal to hexadecimal
        String hexChars = "0123456789ABCDEF";
        StringBuilder hexBuilder = new StringBuilder();
        tempDecimal = decimalNumber;
        while (tempDecimal > 0) {
            int remainder = tempDecimal % 16;
            hexBuilder.insert(0, hexChars.charAt(remainder));
            tempDecimal /= 16;
        }

        // Display results
        System.out.println("Binary Number: " + binaryNumber);
        System.out.println("Decimal Number: " + decimalNumber);
        System.out.println("Octal Number: " + octalNumber);
        System.out.println("Hexadecimal Number: " + hexBuilder.toString());
    }
}