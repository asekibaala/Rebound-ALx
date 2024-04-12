#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "monty.h" // Include your header file where data structures are defined

// Function prototypes
void parse_line(char *line, unsigned int line_number);
void push(stack_t **stack, unsigned int line_number, int value);
void pall(stack_t **stack, unsigned int line_number);

int main(int argc, char *argv[]) {
    FILE *file;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    unsigned int line_number = 0;

    // Check if the correct number of arguments is provided
    if (argc != 2) {
        fprintf(stderr, "USAGE: monty file\n");
        exit(EXIT_FAILURE);
    }

    // Open the Monty bytecode file
    file = fopen(argv[1], "r");
    if (file == NULL) {
        fprintf(stderr, "Error: Can't open file %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    // Read and parse each line of the file
    while ((read = getline(&line, &len, file)) != -1) {
        line_number++;
        parse_line(line, line_number);
    }

    // Close the file
    fclose(file);
    if (line)
        free(line);

    return 0;
}

void parse_line(char *line, unsigned int line_number) {
    // Tokenize the line to separate the opcode and argument
    char *token;
    char *opcode;
    int arg;

    token = strtok(line, " \n");
    if (token == NULL || token[0] == '#') // Skip empty lines and comments
        return;

    opcode = token;

    // Check the opcode and call the corresponding function
    if (strcmp(opcode, "push") == 0) {
        // Extract the argument for push
        token = strtok(NULL, " \n");
        if (token == NULL) {
            fprintf(stderr, "L%d: usage: push integer\n", line_number);
            exit(EXIT_FAILURE);
        }
        arg = atoi(token);
        push(&stack, line_number, arg);
    } else if (strcmp(opcode, "pall") == 0) {
        pall(&stack, line_number);
    } else {
        fprintf(stderr, "L%d: unknown instruction %s\n", line_number, opcode);
        exit(EXIT_FAILURE);
    }
}

void push(stack_t **stack, unsigned int line_number, int value) {
    stack_t *new_node = malloc(sizeof(stack_t));
    if (new_node == NULL) {
        fprintf(stderr, "Error: malloc failed\n");
        exit(EXIT_FAILURE);
    }
    new_node->n = value;
    new_node->prev = NULL;
    new_node->next = *stack;

    if (*stack != NULL) {
        (*stack)->prev = new_node;
    }

    *stack = new_node;
}

void pall(stack_t **stack, unsigned int line_number) {
    stack_t *current = *stack;

    while (current != NULL) {
        printf("%d\n", current->n);
        current = current->next;
    }
}
