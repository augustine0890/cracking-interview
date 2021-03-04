# Practice Java

## Let's Start
- A package is a grouping of Java types (classes of various sorts, including enumeration classes, exception classes and interfaces).
- An example `java.nio.*` package which contains java classes that pertain to certain aspects of file I/O. We have to import this package for use in our program in order to use the classes and methods with which we perform file I/O.
- All code in Java applications is always in class.
- The keyword `public` means that this class is accessible by any other class.
- The file name should also be the name of the contained type, with the extension `.java` applied to it. For example, the class `YourClass` should be in a file named `YourClass.java`.
- A classfile is the result of the Java compilation process applied to a `.java` file. The content of this file is the compiled bytecode that the JVM runs.
- The JVM interprets your classfiles (which contain Java bytecode) and transaltes their contents to instructions for the particular environment. The JVM itself runs directly on the processor.
- Every _class_ that you want to run directly must always have a method named `main`. Classes which do not have a method `main` defined in them cannot be run directly. They can only be used by other classes as components.
- By not putting a method `main` into the `.java` file, we are saying that we do not want its resulting classfile to be directly runnable.

```java
public static void main(String[] args) {
    return;
}
```
- The access modifier `public` gives the method the visiblility for it to be seen and thus be invokable by the JVM.
- The method `main` is always a `static` method.
- The `main` method cannot return a value to the operating sysstem directly and therefore it is assigned a return type of `void`.
- The `return` means exit the method that you are running now and return control back to whoever called this method.

```java
class Man {
    public static String gender="male";
    public String firstName;
    public String lastName;
    public static void main(String[] args){
        Man man01 = new Man(); // We have now created an object named man01 of the class Man
        man01.firstName = "Adam"; // firstName is a "public" field so we can set it in any method
        System.out.println( man01.firstName);
    }
}
```
- A static class member is a member which belongs to the class, whereas an instance memeber belongs to the individual instances of the class.
- Variable number of arguments (varargs)
    - We can pass a varibale number of arguments of a given type to a method designed to receive a variable number of arguments
    - There can only be one variable that can receive a variable number of arguments in a method declaration and it must be the last variable in the method declaration.