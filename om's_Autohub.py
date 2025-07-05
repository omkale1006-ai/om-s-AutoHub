class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Brand:
    def __init__(self, brand):
        self.brand = brand


class BrandShowing:
    def __init__(self):
        self.brands = [
            Brand("1️⃣ Tata Motors"),
            Brand("2️⃣ Mahindra"),
            Brand("3️⃣ Maruti Suzuki"),
            Brand("4️⃣ Hyundai"),
            Brand("5️⃣ Kia"),
            Brand("6️⃣ Electric (EV)")
        ]

    def show_brands(self):
        print("\n🔰 Available Car Brands:")
        for index, brand in enumerate(self.brands, start=1):
            print(f"{index}. {brand.brand}")


class CarShowing:
    def __init__(self):
        self.tatamotors = [
            Car("Tata Punch", 700000),
            Car("Tata Altroz", 750000),
            Car("Tata Nexon", 1100000),
            Car("Tata Harrier", 1600000),
            Car("Tata Safari", 2000000)
        ]
        self.mahindra = [
            Car("Mahindra Bolero", 1000000),
            Car("Mahindra XUV300", 1050000),
            Car("Mahindra Scorpio-N", 1600000),
            Car("Mahindra Thar", 1500000),
            Car("Mahindra XUV700", 2100000)
        ]
        self.maruti_suzuki = [
            Car("Maruti Alto K10", 500000),
            Car("Maruti WagonR", 600000),
            Car("Maruti Swift", 650000),
            Car("Maruti Baleno", 500000),
            Car("Maruti Brezza", 1100000)
        ]
        self.hyundai = [
            Car("Hyundai Grand i10 Nios", 680000),
            Car("Hyundai i20", 850000),
            Car("Hyundai Venue", 1020000),
            Car("Hyundai Creta", 1350000),
            Car("Hyundai Verna", 1300000)
        ]
        self.kia = [
            Car("Kia Sonet", 980000),
            Car("Kia Seltos", 1420000),
            Car("Kia Carens", 1250000)
        ]
        self.electric = [
            Car("Tata Tiago EV", 900000),
            Car("Tata Nexon EV", 1500000),
            Car("MG ZS EV", 2300000),
            Car("Hyundai Kona Electric", 2500000),
            Car("Mahindra XUV400 EV", 1750000)
        ]
        self.order = []

    def show_brand_cars(self, car_list, brand_name):
        print(f"\n🚗 Cars from {brand_name}:")
        for index, item in enumerate(car_list, start=1):
            print(f"{index}. {item.name} - ₹{item.price}")

    def take_order(self, car_list):
        print("\n🛍️ Choose the car you want to order by its number.")
        try:
            choice = int(input("🔢 Enter your choice (1-5) or 0 to finish: "))
            if choice == 0:
                print("✅ Order completed.\n")
            elif 1 <= choice <= len(car_list):
                selected_car = car_list[choice - 1]
                self.order.append(selected_car)
                print(f"✔️ Added to order: {selected_car.name}")
            else:
                print("❌ Invalid choice. Please try again.")
        except ValueError:
            print("⚠️ Please enter a valid number!")

    def show_order(self):
        if not self.order:
            print("🛑 No cars ordered.")
            return
        total = 0
        print("\n🧾 Order Summary:")
        for item in self.order:
            print(f"🚘 {item.name} - ₹{item.price}")
            total += item.price
        print(f"💰 Total Amount: ₹{total}")

    def brand_choose(self):
        print("\n🔧 Choose a Car Brand by Number")
        brand = input("➡️ Enter the brand number (1-6): ")
        if brand == "1":
            self.show_brand_cars(self.tatamotors, "Tata Motors")
            self.take_order(self.tatamotors)
        elif brand == "2":
            self.show_brand_cars(self.mahindra, "Mahindra")
            self.take_order(self.mahindra)
        elif brand == "3":
            self.show_brand_cars(self.maruti_suzuki, "Maruti Suzuki")
            self.take_order(self.maruti_suzuki)
        elif brand == "4":
            self.show_brand_cars(self.hyundai, "Hyundai")
            self.take_order(self.hyundai)
        elif brand == "5":
            self.show_brand_cars(self.kia, "Kia")
            self.take_order(self.kia)
        elif brand == "6":
            self.show_brand_cars(self.electric, "Electric (EV)")
            self.take_order(self.electric)
        else:
            print("❌ Invalid brand choice. Please choose a number between 1-6.")

    def welcome(self):
        print("\n🎉 Welcome to Om's AutoHub!")
        print("🚗 We offer a wide variety of car brands and models.")

    def user_information(self):
        user_name = input("👤 Enter your full name: ").title()

        while True:
            try:
                user_age = int(input("🎂 Enter your age: "))
                if user_age < 18:
                    print("❌ Sorry! You must be at least 18 years old to buy a car.")
                    return False
                break
            except ValueError:
                print("❌ Please enter a valid number for age.")

        user_gender = input("⚧️ Enter your gender: ")
        user_email = input("📧 Enter your email: ")
        user_address = input("🏠 Enter your address: ")
        user_phone = input("📞 Enter your phone number: ")

        print(f"\n✅ Welcome to Om's AutoHub, Mr./Ms. {user_name}!")
        print(f"📋 Your Details: Age - {user_age}, Gender - {user_gender}, Email - {user_email}, Contact - {user_phone}")
        print("✅ Let's explore the cars now!\n")
        return True


def main():
    showroom = CarShowing()
    brands_list = BrandShowing()

    showroom.welcome()

    if showroom.user_information():
        brands_list.show_brands()
        showroom.brand_choose()
        showroom.show_order()
        print("\n🙏 Thank you for visiting Om's AutoHub! Have a great day! 🚗💨")
    else:
        print("⛔ Access Denied: Only users 18 years and older can buy cars.")


if __name__ == "__main__":
    main()
