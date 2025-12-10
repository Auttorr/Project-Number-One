import tkinter as tk 
import threading 
import time 
import keyboard 
import pyautogui 

class AutoClicker: 
    def init(self): 
        self.window = tk.Tk() 
        self.window.title("Autor-Coders AutoClicker") 
        self.window.geometry("400x250") 
        self.window.configure(bg="#1a1a2e") 
        text 

        self.clicking = False 
        self.click_thread = None 
        self.clicks_per_second = 10 

        self.setup_ui() 
        self.setup_hotkeys() 

        def setup_ui(self): 
            title_label = tk.Label( 
                self.window, 
                text="Autor-Coders AutoClicker", 
                font=("Consolas", 18, "bold"), 
                bg="#1a1a2e", 
                fg="#00ff88" 
                ) 
                title_label.pack(pady=15) 

                status_frame = tk.Frame(self.window, bg="#16213e", bd=2, relief="ridge") 
                status_frame.pack(pady=10, padx=20, fill="x") 

                self.status_label = tk.Label( 
                    status_frame, 
                    text="СТАТУС: ВЫКЛЮЧЕНО", 
                    font=("Consolas", 14), 
                    bg="#16213e", 
                    fg="#ff5555" 
                    ) 
                    self.status_label.pack(pady=10) 

                    config_frame = tk.Frame(self.window, bg="#1a1a2e") 
                    config_frame.pack(pady=10) 

                    speed_label = tk.Label( 
                        config_frame, 
                        text="Кликов  секунду:", 
                        font=("Consolas", 12), 
                        bg="#1a1a2e", 
                        fg="#aaddff" 
                        ) 
                        speed_label.grid(row=0, column=0, padx=5, pady=5) 

                        self.speed_var = tk.StringVar(value="10") 
                        self.speed_entry = tk.Entry( 
                            config_frame, 
                            textvariable=self.speed_var, 
                            font=("Consolas", 12), 
                            width=10, 
                            justify="center", 
                            bg="#0f3460", 
                            fg="white", 
                            insertbackground="white" 
                            ) 
                            self.speed_entry.grid(row=0, column=1, padx=5, pady=5) 

                            update_btn = tk.Button( 
                                config_frame, 
                                text="Обновить", 
                                font=("Consolas", 10), 
                                bg="#00aa66", 
                                fg="white", 
                                activebackground="#008855", 
                                command=self.update_speed 
                                ) 
                                update_btn.grid(row=0, column=2, padx=5, pady=5) 

                                hotkey_frame = tk.Frame(self.window, bg="#0f3460", bd=1, relief="solid") 
                                hotkey_frame.pack(pady=15, padx=20, fill="x") 

                                hotkey_label = tk.Label( 
                                    hotkey_frame, 
                                    text="Горячие клавиши:\nF6 - Запуск/Остановка\nF7 - Выход", 
                                    font=("Consolas", 11), 
                                    bg="#0f3460", 
                                    fg="#88ff88", 
                                    justify="center" 
                                    ) 
                                    hotkey_label.pack(pady=10) 

                                    self.clicks_count = 0 
                                    self.clicks_label = tk.Label( 
                                        self.window, 
                                        text=f"Сделано кликов: {self.clicks_count}", 
                                        font=("Consolas", 10), 
                                        bg="#1a1a2e", 
                                        fg="#ffcc00" 
                                        ) 
                                        self.clicks_label.pack(pady=5) 

                                        def setup_hotkeys(self): 
                                            keyboard.add_hotkey('f6', self.toggle_clicking) 
                                            keyboard.add_hotkey('f7', self.exit_program) 

                                            def update_speed(self): 
                                                try: 
                                                    speed = int(self.speed_var.get()) 
                                                    if 1 <= speed <= 1000: 
                                                        self.clicks_per_second = speed 
                                                        self.status_label.config(text=f"СКОРОСТЬ: {speed} клик/сек") 
                                                        else: 
                                                            self.speed_var.set(str(self.clicks_per_second)) 
                                                            except: 
                                                                self.speed_var.set(str(self.clicks_per_second)) 

                                                                def toggle_clicking(self): 
                                                                    if not self.clicking: 
                                                                        self.start_clicking() 
                                                                        else: 
                                                                            self.stop_clicking() 

                                                                            def start_clicking(self): 
                                                                                self.clicking = True 
                                                                                self.status_label.config(text="СТАТУС: АКТИВНО", fg="#00ff88") 
                                                                                self.click_thread = threading.Thread(target=self.click_loop, daemon=True) 
                                                                                self.click_thread.start() 

                                                                                def stop_clicking(self): 
                                                                                    self.clicking = False 
                                                                                    self.status_label.config(text="СТАТУС: ВЫКЛЮЧЕНО", fg="#ff5555") 

                                                                                    def click_loop(self): 
                                                                                        delay = 1.0 / self.clicks_per_second 
                                                                                        while self.clicking: 
                                                                                            try: 
                                                                                                pyautogui.click() 
                                                                                                self.clicks_count += 1 
                                                                                                self.window.after(0, self.update_clicks_label) 
                                                                                                time.sleep(delay) 
                                                                                                except: 
                                                                                                    pass 

                                                                                                def update_clicks_label(self): 
                                                                                                    self.clicks_label.config(text=f"Сделано кликов: {self.clicks_count}") 

                                                                                                    def exit_program(self): 
                                                                                                        self.clicking = False 
                                                                                                        self.window.quit() 
                                                                                                        self.window.destroy() 

                                                                                                        def run(self): 
                                                                                                            self.window.mainloop() 

                                                                                                            if name == "main": 
                                                                                                                clicker = AutoClicker() 
                                                                                                                clicker.run() 
