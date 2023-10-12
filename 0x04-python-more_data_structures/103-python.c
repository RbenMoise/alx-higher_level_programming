#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var_obj = (PyVarObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", var_obj->ob_size);
    printf("[*] Allocated = %ld\n", var_obj->ob_alloc);
    
    for (Py_ssize_t i = 0; i < var_obj->ob_size; i++) {
        PyObject *item = list->ob_item[i];
        printf("Element %ld: ", i);
        
        if (PyBytes_Check(item)) {
            printf("bytes\n");
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_GET_SIZE(item));
            
            if (PyBytes_GET_SIZE(item) > 10) {
                printf("  trying string: %s\n", PyBytes_AsString(item));
                printf("  first 10 bytes: ");
                for (Py_ssize_t j = 0; j < 10; j++) {
                    printf("%02x ", (unsigned char)PyBytes_AS_STRING(item)[j]);
                }
                printf("\n");
            } else {
                printf("  trying string: %s\n", PyBytes_AsString(item));
                printf("  first %ld bytes: ", PyBytes_GET_SIZE(item));
                for (Py_ssize_t j = 0; j < PyBytes_GET_SIZE(item); j++) {
                    printf("%02x ", (unsigned char)PyBytes_AS_STRING(item)[j]);
                }
                printf("\n");
            }
        } else if (PyFloat_Check(item)) {
            printf("float\n");
        } else if (PyLong_Check(item)) {
            printf("int\n");
        } else if (PyTuple_Check(item)) {
            printf("tuple\n");
        } else if (PyList_Check(item)) {
            printf("list\n");
        } else if (PyUnicode_Check(item)) {
            printf("str\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_GET_SIZE(p));
    
    if (PyBytes_GET_SIZE(p) > 10) {
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first 10 bytes: ");
        for (Py_ssize_t i = 0; i < 10; i++) {
            printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
        }
        printf("\n");
    } else {
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first %ld bytes: ", PyBytes_GET_SIZE(p));
        for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p); i++) {
            printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
        }
        printf("\n");
    }
}

