rooms = {
    101: {
        "room_type": "Single",
        "price_per_night": 100,
        "occupants": [
            {"name": "John Doe", "check_in": "2025-02-01", "check_out": "2025-02-07", "email": "johndoe@example.com", "phone": "+1234567890", "special_requests": "Near elevator, extra pillows"},
            {"name": "Sarah Miller", "check_in": "2025-02-08", "check_out": "2025-02-15", "email": "sarahmiller@example.com", "phone": "+0987654321", "special_requests": "Quiet room, allergy-free bedding"},
            {"name": "Liam Smith", "check_in": "2025-02-16", "check_out": "2025-02-23", "email": "liamsmith@example.com", "phone": "+1777888999", "special_requests": "Late check-out, high floor"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": False}
    },
    102: {
        "room_type": "Double",
        "price_per_night": 150,
        "occupants": [
            {"name": "Jane Smith", "check_in": "2025-02-03", "check_out": "2025-02-10", "email": "janesmith@example.com", "phone": "+1122334455", "special_requests": "King-sized bed, extra towels"},
            {"name": "Michael Brown", "check_in": "2025-02-11", "check_out": "2025-02-17", "email": "michaelbrown@example.com", "phone": "+1444556677", "special_requests": "Close to pool, extra blankets"},
            {"name": "Emily Davis", "check_in": "2025-02-18", "check_out": "2025-02-24", "email": "emilydavis@example.com", "phone": "+1999888777", "special_requests": "Late check-in, extra pillows"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True}
    },
    103: {
        "room_type": "Suite",
        "price_per_night": 250,
        "occupants": [
            {"name": "Mike Johnson", "check_in": "2025-02-05", "check_out": "2025-02-12", "email": "mikejohnson@example.com", "phone": "+1555443322", "special_requests": "Romantic setup, rose petals"},
            {"name": "Anna Williams", "check_in": "2025-02-13", "check_out": "2025-02-20", "email": "annawilliams@example.com", "phone": "+1999222333", "special_requests": "Jacuzzi setup, room service"},
            {"name": "James Wilson", "check_in": "2025-02-21", "check_out": "2025-02-28", "email": "jameswilson@example.com", "phone": "+1888777666", "special_requests": "Additional towels, extra pillows"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True, "jacuzzi": True}
    },
    104: {
        "room_type": "Single",
        "price_per_night": 100,
        "occupants": [
            {"name": "Alice Cooper", "check_in": "2025-02-01", "check_out": "2025-02-10", "email": "alicecooper@example.com", "phone": "+1222333444", "special_requests": "Wheelchair accessible room"},
            {"name": "Bob Martin", "check_in": "2025-02-11", "check_out": "2025-02-17", "email": "bobmartin@example.com", "phone": "+1777888999", "special_requests": "Quiet room, extra lighting"},
            {"name": "Claire Stevens", "check_in": "2025-02-18", "check_out": "2025-02-24", "email": "clairestevens@example.com", "phone": "+1888777766", "special_requests": "Pet-friendly room, extra towels"}
        ],
        "extras": {"wifi": True, "air_conditioning": False, "mini_bar": False}
    },
    105: {
        "room_type": "Double",
        "price_per_night": 150,
        "occupants": [
            {"name": "John Black", "check_in": "2025-02-03", "check_out": "2025-02-08", "email": "johnblack@example.com", "phone": "+1234432111", "special_requests": "Late check-out, quiet room"},
            {"name": "Laura Green", "check_in": "2025-02-09", "check_out": "2025-02-16", "email": "lauragreen@example.com", "phone": "+1444332211", "special_requests": "Early check-in, extra bed"},
            {"name": "Sophia Evans", "check_in": "2025-02-17", "check_out": "2025-02-24", "email": "sophiaevans@example.com", "phone": "+1999776655", "special_requests": "Non-smoking room, extra blankets"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True}
    },
    106: {
        "room_type": "Suite",
        "price_per_night": 250,
        "occupants": [
            {"name": "Tom Harris", "check_in": "2025-02-05", "check_out": "2025-02-15", "email": "tomharris@example.com", "phone": "+1444332211", "special_requests": "Jacuzzi setup"},
            {"name": "Nina Jones", "check_in": "2025-02-16", "check_out": "2025-02-25", "email": "ninajones@example.com", "phone": "+1555443322", "special_requests": "Extra towels"},
            {"name": "Mark Taylor", "check_in": "2025-02-26", "check_out": "2025-03-05", "email": "marktaylor@example.com", "phone": "+1666777888", "special_requests": "Late check-out"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True, "jacuzzi": True}
    },
    107: {
        "room_type": "Single",
        "price_per_night": 100,
        "occupants": [
            {"name": "Evan Clark", "check_in": "2025-02-01", "check_out": "2025-02-07", "email": "evanclark@example.com", "phone": "+1222333444", "special_requests": "Extra pillows"},
            {"name": "Olivia Adams", "check_in": "2025-02-08", "check_out": "2025-02-14", "email": "oliviaadams@example.com", "phone": "+1555443322", "special_requests": "Late check-out"},
            {"name": "Gabriel Lee", "check_in": "2025-02-15", "check_out": "2025-02-22", "email": "gabriellee@example.com", "phone": "+1444556677", "special_requests": "Quiet room"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": False}
    },
    108: {
        "room_type": "Double",
        "price_per_night": 150,
        "occupants": [
            {"name": "James Miller", "check_in": "2025-02-10", "check_out": "2025-02-17", "email": "jamesmiller@example.com", "phone": "+1222333444", "special_requests": "King-sized bed, extra pillows"},
            {"name": "Ella White", "check_in": "2025-02-18", "check_out": "2025-02-24", "email": "ella@example.com", "phone": "+1444332211", "special_requests": "Room with a view"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True}
    },
    109: {
        "room_type": "Suite",
        "price_per_night": 250,
        "occupants": [
            {"name": "Jack King", "check_in": "2025-02-01", "check_out": "2025-02-10", "email": "jackking@example.com", "phone": "+1122334455", "special_requests": "Jacuzzi setup, champagne"},
            {"name": "Sophia Clark", "check_in": "2025-02-12", "check_out": "2025-02-22", "email": "sophiaclark@example.com", "phone": "+1999776655", "special_requests": "Early check-in"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True, "jacuzzi": True}
    },
    110: {
        "room_type": "Single",
        "price_per_night": 100,
        "occupants": [
            {"name": "Linda Brown", "check_in": "2025-02-05", "check_out": "2025-02-10", "email": "lindabrown@example.com", "phone": "+1222333444", "special_requests": "Extra towels"},
            {"name": "David White", "check_in": "2025-02-11", "check_out": "2025-02-16", "email": "davidwhite@example.com", "phone": "+1444556677", "special_requests": "Extra blankets"}
        ],
        "extras": {"wifi": True, "air_conditioning": False, "mini_bar": False}
    },
    111: {
        "room_type": "Double",
        "price_per_night": 150,
        "occupants": [
            {"name": "Julia Parker", "check_in": "2025-02-15", "check_out": "2025-02-22", "email": "juliaparker@example.com", "phone": "+1222333444", "special_requests": "Late check-out"},
            {"name": "Ryan Hill", "check_in": "2025-02-23", "check_out": "2025-02-28", "email": "ryanhill@example.com", "phone": "+1444332211", "special_requests": "Pet-friendly"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True}
    },
    112: {
        "room_type": "Suite",
        "price_per_night": 250,
        "occupants": [
            {"name": "Olivia King", "check_in": "2025-02-01", "check_out": "2025-02-12", "email": "oliviaking@example.com", "phone": "+1999776655", "special_requests": "Jacuzzi setup"},
            {"name": "Lucas Collins", "check_in": "2025-02-13", "check_out": "2025-02-19", "email": "lucascollins@example.com", "phone": "+1222333444", "special_requests": "Extra towels, extra pillows"},
            {"name": "Nina Carter", "check_in": "2025-02-20", "check_out": "2025-02-25", "email": "ninacarter@example.com", "phone": "+1444332211", "special_requests": "High floor"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True, "jacuzzi": True}
    },
    113: {
        "room_type": "Single",
        "price_per_night": 100,
        "occupants": [
            {"name": "Jared Scott", "check_in": "2025-02-03", "check_out": "2025-02-07", "email": "jaredscott@example.com", "phone": "+1444332211", "special_requests": "Extra towels"}
        ],
        "extras": {"wifi": True, "air_conditioning": False, "mini_bar": False}
    },
    114: {
        "room_type": "Double",
        "price_per_night": 150,
        "occupants": [
            {"name": "Chloe Gray", "check_in": "2025-02-09", "check_out": "2025-02-15", "email": "chloejones@example.com", "phone": "+1888777666", "special_requests": "Extra pillows"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": False}
    },
    115: {
        "room_type": "Suite",
        "price_per_night": 250,
        "occupants": [
            {"name": "Johnathan White", "check_in": "2025-02-01", "check_out": "2025-02-14", "email": "johnathanwhite@example.com", "phone": "+1555443322", "special_requests": "Champagne and Jacuzzi"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True, "jacuzzi": True}
    },
    116: {
        "room_type": "Single",
        "price_per_night": 100,
        "occupants": [
            {"name": "Tommy Blake", "check_in": "2025-02-01", "check_out": "2025-02-05", "email": "tommyblake@example.com", "phone": "+1222333444", "special_requests": "Extra blankets"},
            {"name": "Rebecca Brooks", "check_in": "2025-02-06", "check_out": "2025-02-10", "email": "rebeccabrooks@example.com", "phone": "+1444556677", "special_requests": "Late check-out"},
            {"name": "Marcus Evans", "check_in": "2025-02-11", "check_out": "2025-02-15", "email": "marcusevans@example.com", "phone": "+1555443322", "special_requests": "Extra pillows"}
        ],
        "extras": {"wifi": True, "air_conditioning": False, "mini_bar": False}
    },
    117: {
        "room_type": "Double",
        "price_per_night": 150,
        "occupants": [
            {"name": "Oliver Green", "check_in": "2025-02-02", "check_out": "2025-02-08", "email": "olivergreen@example.com", "phone": "+1444332211", "special_requests": "Non-smoking room"},
            {"name": "Sophia Harris", "check_in": "2025-02-09", "check_out": "2025-02-14", "email": "sophiaharris@example.com", "phone": "+1888777666", "special_requests": "Extra towels"},
            {"name": "Ethan Lewis", "check_in": "2025-02-15", "check_out": "2025-02-22", "email": "ethanlewis@example.com", "phone": "+1999888777", "special_requests": "Room with a view"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True}
    },
    118: {
        "room_type": "Suite",
        "price_per_night": 250,
        "occupants": [
            {"name": "Liam Scott", "check_in": "2025-02-05", "check_out": "2025-02-12", "email": "liamscott@example.com", "phone": "+1222333444", "special_requests": "Jacuzzi and room service"},
            {"name": "Emma Young", "check_in": "2025-02-13", "check_out": "2025-02-18", "email": "emmayoung@example.com", "phone": "+1444556677", "special_requests": "Champagne upon arrival"},
            {"name": "Lucas King", "check_in": "2025-02-19", "check_out": "2025-02-26", "email": "lucasking@example.com", "phone": "+1555443322", "special_requests": "Early check-in, extra pillows"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True, "jacuzzi": True}
    },
    119: {
        "room_type": "Single",
        "price_per_night": 100,
        "occupants": [
            {"name": "Ava Collins", "check_in": "2025-02-03", "check_out": "2025-02-07", "email": "avacollins@example.com", "phone": "+1222333444", "special_requests": "Pet-friendly room"},
            {"name": "Benjamin Clark", "check_in": "2025-02-08", "check_out": "2025-02-13", "email": "benjaminclark@example.com", "phone": "+1444556677", "special_requests": "Quiet room"}
        ],
        "extras": {"wifi": True, "air_conditioning": False, "mini_bar": False}
    },
    120: {
        "room_type": "Double",
        "price_per_night": 150,
        "occupants": [
            {"name": "Grace Hill", "check_in": "2025-02-01", "check_out": "2025-02-06", "email": "gracehill@example.com", "phone": "+1222333444", "special_requests": "Extra bed"},
            {"name": "Matthew Moore", "check_in": "2025-02-07", "check_out": "2025-02-14", "email": "matthewmoore@example.com", "phone": "+1444556677", "special_requests": "Close to the gym"},
            {"name": "Charlotte Allen", "check_in": "2025-02-15", "check_out": "2025-02-22", "email": "charlotteallen@example.com", "phone": "+1555443322", "special_requests": "Extra blankets, quiet room"}
        ],
        "extras": {"wifi": True, "air_conditioning": True, "mini_bar": True}
    }
}

