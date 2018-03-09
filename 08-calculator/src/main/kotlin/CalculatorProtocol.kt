package main.kotlin

/**
 * Protocol used for communication between CalculatorClient and Server.
 *
 * @author Markus Reichl <mreichl-tgm@re1.at>
 */

@Throws(NumberFormatException::class)
fun process(input: String): Any? {
    when {
        input.contains("!add")  -> return add(input)
        input.contains("!sub")  -> return sub(input)
        input.contains("!help") ->
            return  "[!add] Sum up given numbers, " +
                    "[!sub] Subtract given numbers from the first element, " +
                    "[!buy] Buy given number of credits, " +
                    "[!help] Shows this help"
    }

    return null
}

@Throws(NumberFormatException::class)
fun add(input: String): Float? {
    return input
            .substringAfter("!add ")
            .split(" ", ",", " + ")
            .map { it.toFloat() }.sum()
}

@Throws(NumberFormatException::class)
fun sub(input: String): Float? {
    val args = input
            .substringAfter("!sub ")
            .split(" ", ",", " - ")
            .map { it.toFloat() }

    return args[0] - args.drop(1).sum()
}