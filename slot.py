import tkinter as tk
import random

symbols = [
    "🍒","🍋","🍉","🍇","🍎",
    "🔔","⭐","💎","🍀","🔥",
    "🎲","🎯","🎰","💰","🪙",
    "👑","⚡","🌈","🍩","🍭"
]

spinning = False
final_result = []

def spin_column(label, final_symbol, count, is_last=False):
    if count > 0:
        label.config(text=random.choice(symbols))
        root.after(80, spin_column, label, final_symbol, count - 1, is_last)
    else:
        label.config(text=final_symbol)

        # ✅ CHỈ CỘT CUỐI MỚI ĐƯỢC BÁO KẾT QUẢ
        if is_last:
            show_result()

def start_spin():
    global spinning, final_result
    if spinning:
        return

    spinning = True
    result_label.config(text="")
    spin_button.config(state="disabled")

    # 🎯 QUYẾT ĐỊNH KẾT QUẢ TRƯỚC
    final_result = [random.choice(symbols) for _ in range(3)]

    # 🎰 QUAY TỪNG CỘT
    spin_column(slot1, final_result[0], 15)
    root.after(300, spin_column, slot2, final_result[1], 18)
    root.after(600, spin_column, slot3, final_result[2], 21, True)

def show_result():
    global spinning

    if final_result[0] == final_result[1] == final_result[2]:
        result_label.config(text="🎉 JACKPOT!!! 🎉", fg="#00ff99")
    else:
        result_label.config(text="🐔 GÀ", fg="#ff6666")

    spin_button.config(state="normal")
    spinning = False

# ===== GUI =====
root = tk.Tk()
root.title("🎰  Slot Machine")
root.geometry("420x320")
root.configure(bg="#1b1b1b")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🎰 SLOT MACHINE 🎰",
    font=("Arial", 16, "bold"),
    bg="#1b1b1b",
    fg="#ffd700"
)
title.pack(pady=10)

slot_frame = tk.Frame(root, bg="#333333", bd=5, relief="ridge")
slot_frame.pack(pady=20)

slot_font = ("Segoe UI Emoji", 42)

slot1 = tk.Label(slot_frame, text="❓", font=slot_font, width=2, bg="black", fg="white")
slot1.pack(side="left", padx=10, pady=10)

slot2 = tk.Label(slot_frame, text="❓", font=slot_font, width=2, bg="black", fg="white")
slot2.pack(side="left", padx=10, pady=10)

slot3 = tk.Label(slot_frame, text="❓", font=slot_font, width=2, bg="black", fg="white")
slot3.pack(side="left", padx=10, pady=10)

spin_button = tk.Button(
    root,
    text="🎲 SPIN 🎲",
    font=("Arial", 14, "bold"),
    bg="#ffd700",
    fg="black",
    command=start_spin
)
spin_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#1b1b1b"
)
result_label.pack(pady=10)

root.mainloop()
