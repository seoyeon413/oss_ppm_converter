def convert_p6_to_p3(input_file, output_file):
    with open(input_file, "rb") as f:
        magic_number = f.readline().strip()
        if magic_number != b'P6':
            raise ValueError("Not a P6 PPM file")

        def read_non_comment_line():
            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()
            return line

        width_height = read_non_comment_line()
        width, height = map(int, width_height.strip().split())

        maxval_line = read_non_comment_line()
        maxval = int(maxval_line.strip())

        pixel_data = f.read()

    with open(output_file, "w") as out:
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{maxval}\n")

        for i in range(0, len(pixel_data), 3):
            r = pixel_data[i]
            g = pixel_data[i+1]
            b = pixel_data[i+2]
            out.write(f"{r} {g} {b}\n")

# 실행
convert_p6_to_p3("colorP6File.ppm", "colorP3File.ppm")

