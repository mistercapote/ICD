#Definir niveis da forca
def dead_levels(tries, usuario):
    deading = [
        f"""
                   --------
                   |      |
                   |      
                   |     ___
                   |    /  ✝  \\
                   |    |  RIP |
                   |    |{usuario}|
                   ----------------
        """,

        """
                   --------  
                   |      |
                   |      O
                   |     
                   |      
                   |      
                   |     
                   ----------------
        """,
        """
                   -------- 
                   |      |
                   |      O
                   |      |
                   |      |
                   |      
                   |     
                   ----------------
        """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |      
                   |     
                   ----------------
        """,
        """
                   --------   
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   |     
                   ----------------
        """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   |     
                   ----------------
        """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   |     
                   ----------------
        """,
        """
                        *****
                    *       *
                    *  ^   ^  *
                    *    \_/    *
                    *  \___/  *
                    *       *
                    *****
                        |
                        |
                        +++
                        | |
                        +++
        """
    ]
    return deading[tries]