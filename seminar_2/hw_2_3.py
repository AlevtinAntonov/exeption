# 3. Дан следующий код, исправьте его там, где требуется
# Задание 3
#
# public static void main(String[] args) throws Exception {
#    try {
#        int a = 90;
#        int b = 3;
#        System.out.println(a / b);
#        printSum(23, 234);
#        int[] abc = { 1, 2 };
#        abc[3] = 9;
#    } catch (Throwable ex) {
#        System.out.println("Что-то пошло не так...");
#    } catch (NullPointerException ex) {
#        System.out.println("Указатель не может указывать на null!");
#    } catch (IndexOutOfBoundsException ex) {
#        System.out.println("Массив выходит за пределы своего размера!");
#    }
# }
# public static void printSum(Integer a, Integer b) throws FileNotFoundException {
#    System.out.println(a + b);
# }
try:
    a = 90
    b = 1
    print(a / b)
    print(23 + 234)
    abc = [1, 2]
    abc[3] = 9
except ZeroDivisionError as e:
    print(f"Указатель не может указывать на null! - {e}")
except IndexError as e:
    print(f"Массив выходит за пределы своего размера! - {e}")
except Exception as e:
    print(f"Что-то пошло не так... {e}")
