import tkinter as tk
from tkinter import messagebox, scrolledtext
import time

def calculateLcsLength(string1, string2):
    """
    Calcula a tabela de comprimentos da Subsequência Comum Mais Longa (LCS)
    entre duas strings usando programação dinâmica.
    """
    # Obtém os comprimentos das duas strings
    len_string1, len_string2 = len(string1), len(string2)

    # Cria a tabela DP inicializada com zeros
    dp = [[0] * (len_string2 + 1) for _ in range(len_string1 + 1)]

    # Preenche a tabela DP iterando sobre cada caractere das duas strings
    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):

            # Se os caracteres são iguais, adiciona 1 ao valor da diagonal superior esquerda
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            # Se são diferentes, escolhe o maior valor entre o de cima e o da esquerda
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Retorna a tabela DP completa
    return dp

def all_lcs_without_backtracking(string1, string2, len_dp):
    n, m = len(string1), len(string2)
    
    # Construir tabela dp com os conjuntos de LCS
    result_dp = [[set() for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        result_dp[i][0].add("")  # Borda: LCS com string vazia é ""
    for j in range(m + 1):
        result_dp[0][j].add("")  # Borda: LCS com string vazia é ""
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i-1] == string2[j-1]:
                # Se os caracteres são iguais, extendemos as sequências de dp[i-1][j-1]
                for seq in result_dp[i-1][j-1]:
                    result_dp[i][j].add(seq + string1[i-1])
            else:
                # Se diferentes, incluímos sequências do maior comprimento
                if len_dp[i-1][j] == len_dp[i][j]:
                    result_dp[i][j].update(result_dp[i-1][j])
                if len_dp[i][j-1] == len_dp[i][j]:
                    result_dp[i][j].update(result_dp[i][j-1])
    
    return result_dp[n][m]

# Classe para a interface gráfica
class LCSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculador de LCS")
        self.create_widgets()
    
    def create_widgets(self):
        # Rótulo e campo para o número de conjuntos de dados
        tk.Label(self.root, text="Número de conjuntos de dados:").grid(row=1, column=0, sticky='w')
        self.num_sets_entry = tk.Entry(self.root)
        self.num_sets_entry.grid(row=1, column=1, sticky='w')
        
        # Botão para gerar os campos de entrada
        self.generate_button = tk.Button(self.root, text="Gerar campos", command=self.generate_input_fields)
        self.generate_button.grid(row=2, column=0, columnspan=2)
        
        # Canvas com scrollbar para os campos de entrada
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.input_frame = tk.Frame(self.canvas)
        
        # Configurar a rolagem
        self.input_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.input_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Posicionar canvas e scrollbar
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=1)

        self.canvas.grid(row=3, column=0, columnspan=2, sticky='nsew')
        self.scrollbar.grid(row=3, column=2, sticky='ns')
        
        # Botão para calcular as LCS
        self.calculate_button = tk.Button(self.root, text="Calcular LCS", command=self.calculate_lcs)
        self.calculate_button.grid(row=4, column=0, columnspan=2)
        
        # Área de texto para exibir os resultados com rolagem horizontal e sem quebra de linha
        self.result_text = tk.Text(self.root, width=40, height=10, wrap=tk.NONE, state='disabled')
        self.result_vscrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.result_text.yview)
        self.result_hscrollbar = tk.Scrollbar(self.root, orient="horizontal", command=self.result_text.xview)
        self.result_text.configure(yscrollcommand=self.result_vscrollbar.set, xscrollcommand=self.result_hscrollbar.set)
        self.result_text.grid(row=5, column=0, columnspan=2, sticky='nsew')
        self.result_vscrollbar.grid(row=5, column=2, sticky='ns')
        self.result_hscrollbar.grid(row=6, column=0, columnspan=2, sticky='ew')
        
        # Rótulo para exibir o tempo de execução
        self.time_label = tk.Label(self.root, text="Tempo de execução: N/A")
        self.time_label.grid(row=7, column=0, columnspan=2)

        self.input_frame.bind("<MouseWheel>", self._on_mousewheel)

    def generate_input_fields(self):
        # Limpar o frame existente
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        try:
            num_sets = int(self.num_sets_entry.get())
            if num_sets <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro positivo para o número de conjuntos.")
            return

        self.string_entries = []
        for i in range(num_sets):
            tk.Label(self.input_frame, text=f"Conjunto {i+1} - String 1:").grid(row=i*2, column=0, sticky='e')
            entry1 = tk.Entry(self.input_frame, width=100)
            entry1.grid(row=i*2, column=1, sticky='w')
            tk.Label(self.input_frame, text=f"Conjunto {i+1} - String 2:").grid(row=i*2+1, column=0, sticky='e')
            entry2 = tk.Entry(self.input_frame, width=100)
            entry2.grid(row=i*2+1, column=1, sticky='w')
            entry1.bind("<MouseWheel>", self._on_mousewheel)
            entry2.bind("<MouseWheel>", self._on_mousewheel)
            self.string_entries.append((entry1, entry2))

        # Atualizar a região de rolagem
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def calculate_lcs(self):
        if not hasattr(self, 'string_entries') or not self.string_entries:
            messagebox.showerror("Erro", "Por favor, gere os campos de entrada primeiro.")
            return

        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)

        # Iniciar a medição do tempo
        start_time = time.time()

        for idx, (entry1, entry2) in enumerate(self.string_entries):
            s1 = entry1.get().strip().lower()
            s2 = entry2.get().strip().lower()
            if not s1 or not s2 or s1 == "" or s2 == "":
                messagebox.showerror("Erro", "Todos os campos de entrada devem estar preenchidos.")
                return

            dp = calculateLcsLength(s1, s2)
            lcs_set = all_lcs_without_backtracking(s1, s2, dp)
            
            if lcs_set:
                for sub in sorted(lcs_set):
                    self.result_text.insert(tk.END, sub + "\n")
                if idx < len(self.string_entries) - 1:
                    self.result_text.insert(tk.END, "\n")

        end_time = time.time()
        execution_time = end_time - start_time
        
        # Atualizar o rótulo com o tempo de execução
        self.time_label.config(text=f"Tempo de execução: {execution_time:.4f} segundos")
        
        self.result_text.config(state='disabled')

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = LCSApp(root)
    root.mainloop()