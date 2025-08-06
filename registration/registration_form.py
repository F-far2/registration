import flet as ft
import csv
import os

def main(page: ft.Page):
    page.title = "ระบบรับสมัครเข้าร่วมกิจกรรม"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.bgcolor = ft.Colors.BLUE_50

    title = ft.Text(
        value="ฟอร์มรับสมัคร",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_800,
        text_align=ft.TextAlign.CENTER
    )

    name_field = ft.TextField(
        label="ชื่อ - สกุล",
        prefix_icon=ft.Icons.PERSON,
        filled=True,
        border_radius=8
    )

    phone_field = ft.TextField(
        label="หมายเลขโทรศัพท์",
        prefix_icon=ft.Icons.PHONE,
        filled=True,
        border_radius=8,
        keyboard_type=ft.KeyboardType.NUMBER  # ใช้ตัวเลข
    )

    team_field = ft.TextField(
        label="ชื่อทีม",
        prefix_icon=ft.Icons.GROUP,
        filled=True,
        border_radius=8
    )

    output_text = ft.Text(color=ft.Colors.GREEN, size=14)

    def save_data(e):
        name = name_field.value.strip()
        phone = phone_field.value.strip()
        team = team_field.value.strip()

        if name == "" or phone == "" or team == "":
            output_text.value = "❌ กรุณากรอกข้อมูลให้ครบทุกช่อง"
            output_text.color = ft.Colors.RED
        else:
            file_exists = os.path.isfile("registration_data.csv")
            with open("registration_data.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["ชื่อ - สกุล", "หมายเลขโทรศัพท์", "ชื่อทีม"])
                writer.writerow([name, phone, team])
            output_text.value = "✅ บันทึกข้อมูลเรียบร้อยแล้ว"
            output_text.color = ft.Colors.GREEN

            name_field.value = ""
            phone_field.value = ""
            team_field.value = ""

        page.update()

    submit_btn = ft.ElevatedButton(
        text="บันทึก",
        icon=ft.Icons.SAVE,
        on_click=save_data,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=20,
            bgcolor=ft.Colors.BLUE_800,
            color=ft.Colors.WHITE
        )
    )

    page.add(
        title,
        ft.Divider(),
        name_field,
        phone_field,
        team_field,
        submit_btn,
        output_text
    )

ft.app(target=main)
