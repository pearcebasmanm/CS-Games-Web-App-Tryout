export default function Home() {
  return (
    <div className="flex flex-col items-center justify-between min-h-screen text-center text-white bg-black/50 px-6 py-12">
      {/* Hero Section */}
      <div className="max-w-4xl p-12 rounded-xl backdrop-blur-md bg-white/10 shadow-lg space-y-6">
        <h1 className="text-6xl font-bold">Welcome to Grand Lego Hotel</h1>
        <p className="text-xl">
          Step into a world of elegance and creativity. At Grand Lego Hotel, we
          combine luxury, comfort, and unparalleled service to ensure an unforgettable
          experience. Whether you’re seeking a serene getaway or an action-packed
          retreat, we offer everything you need for a dream vacation.
        </p>
        <a href="/booking" className="px-8 py-4 bg-yellow-500 text-xl rounded-lg hover:bg-yellow-600 transition">
          Book Your Stay
        </a>
      </div>

      {/* Features Section */}
      <div className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-12 max-w-6xl">
        <div className="p-8 bg-white/10 rounded-lg shadow-md space-y-2">
          <h2 className="text-2xl font-semibold">🌊 Beachfront Views</h2>
          <p className="text-lg">
            Unwind in one of our exquisite beachfront suites, where the gentle sound
            of crashing waves meets the sight of a breathtaking horizon. Whether you're
            enjoying a quiet moment on your private balcony or lounging in your room,
            the ocean’s beauty will be the backdrop to your perfect escape.
          </p>
        </div>

        <div className="p-8 bg-white/10 rounded-lg shadow-md space-y-2">
          <h2 className="text-2xl font-semibold">🍽️ Fine Dining</h2>
          <p className="text-lg">
            Indulge your senses with a culinary journey like no other. Our world-class
            chefs craft gourmet dishes that blend local flavors with international
            techniques. From intimate dinners by the sea to grand feasts in our elegant
            dining room, every meal promises to be a memorable occasion.
          </p>
        </div>

        <div className="p-8 bg-white/10 rounded-lg shadow-md space-y-2">
          <h2 className="text-2xl font-semibold">🏊‍♂️ Infinity Pool</h2>
          <p className="text-lg">
            Dive into pure bliss in our stunning infinity pool, where the water blends
            seamlessly with the ocean in the distance. Whether you're swimming laps or
            simply lounging by the water's edge, the serene atmosphere will refresh your
            body and soul, offering a perfect way to relax and rejuvenate.
          </p>
        </div>
      </div>

      <div className="p-8 bg-white/10 rounded-lg shadow-md space-y-2">
          <h2 className="text-2xl font-semibold">🧩 Lego Building Fun</h2>
          <p className="text-lg">
            Unleash your creativity with our exclusive Lego building workshops. Perfect for families and
            enthusiasts, where you can build amazing structures and enjoy a fun, hands-on experience.
          </p>
        </div>

      {/* Footer or any additional section */}
      <div className="mt-20 w-full bg-black/60 py-6">
        <p className="text-sm text-white text-center">
          © 2025 Grand Lego Hotel. All rights reserved.
        </p>
      </div>
    </div>
  );
}
