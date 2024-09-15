# Prompts
generate_initial_code = ("You are a beginner in C++. You are given the following question to solve. Provide the brute force method. Just provide the function, no need of the driver function."
                         "Do not provide the most optimized approach in the beginning. First, provide the most naive brute force approach (if there exists one) "
                         "that a beginner in C++ would write, which typically has high time complexity and high space complexity."
                         "Question: {} \n I repeat, do not give the most optimized approach initially. "
                         "Focus on finding a brute force method that takes very high time and space complexity.")

performance_analysis = ("You are a performance analyzer. Analyze the following code for performance issues and suggest optimizations. Just suggest the optimizations, do not provide the code."
                              "\nCode:\n {} \n")

optimize = ("You are an optimizing tool. Optimize the performance, i.e., the time and space complexity, "
            "of the following code and provide the optimized code in C++. Code: \n {} \n Do not provide the most optimized approach "
            "in the beginning. Instead, improve the current approach step by step.")


rating = ("Rate the performance improvements on a scale of 1 to 10 . No need of any extra comments. :"
                "\nCode:\n {}")

performance_comparison = ("Compare the performance before and after the optimizations. Provide ratings on a scale of 1 to 10 for both versions. "
                          "Optimized Code:\n {}\n Original Code:\n {}")

determination = ("Determine if the current code is in it's most optimized version, and can't be optimized further in terms of time and space complexity. "
                 "If yes, return the string TRUE, else return FALSE"
                 "\n Code: {}\n")


