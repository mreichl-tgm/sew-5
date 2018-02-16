package main.kotlin

import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.ServerSocket
import java.net.Socket
import kotlin.system.exitProcess

class CalculatorServer(port: Int) {
    init {
        try {
            val serverSocket = ServerSocket(port)
            // Log success
            println("Server running on 127.0.0.1:" + port)
            // Listen for client connections
            while (!serverSocket.isClosed) {
                CalculatorClientHandler(serverSocket.accept()).start()
                println("Client connected")
            }
        } catch (e: IOException) {
            exitProcess(1)
        }
    }
}

class CalculatorClientHandler(private var socket: Socket,
                              private var credits: Int = 10) : Thread() {
    override fun run() {
        try {
            val reader = BufferedReader(InputStreamReader(socket.getInputStream()))
            val writer = PrintWriter(socket.getOutputStream(), true)

            var inputLine: String?

            while (!socket.isClosed) {
                inputLine = reader.readLine()
                // Check if connection shall be closed
                if (inputLine == null || inputLine.contains("!exit")) break

                println("Client: " + inputLine)

                try {
                    if (inputLine.contains("!buy")) {
                        credits += inputLine
                                .substringAfter("!buy ")
                                .split(" ", ",")
                                .map { it.toInt() }.sum()

                        writer.println("Credits: " + credits)
                    } else {
                        if (inputLine.contains("!add") || inputLine.contains("!sub"))
                            if (credits < 1) {
                                writer.println("Out of credits! Type !buy")
                                continue
                            } else credits--

                        val result = process(inputLine)

                        if (result == null) writer.println("Invalid input. Type !help.")
                        else writer.println(result.toString())
                    }
                } catch (e: NumberFormatException) {
                    writer.println("At least one arguments was not a number")
                }
            }

            println("Client disconnected")
            socket.close()  // Close socket connection after loop
        } catch (e: IOException) {
            e.printStackTrace()
        }
    }
}

fun main(args: Array<String>) {
    CalculatorServer(12345)
}
