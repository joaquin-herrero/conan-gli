from conans import ConanFile, tools


class GliConan(ConanFile):
    name = "gli"
    version = "0.8.2.0"
    license = "The Happy Bunny License (Modified MIT License)"
    author = "Joaquin Herrero Herrero"
    url = "https://github.com/joaquin-herrero/conan-gli"
    description = "Recipe for OpenGL Image. GLI is a header only C++ image library for graphics software"
    topics = ("opengl", "image")
    no_copy_source = True
    requires = "glm:g-truc/0.9.8.5@bincrafters/stable"
    # No settings/options are necessary, this is header only

    def source(self):
        zip_file = "%s.zip" % self.version
        url = "https://github.com/g-truc/gli/archive/%s" % zip_file

        tools.download(url, zip_file)
        tools.unzip(zip_file)

    def package(self):
        source_subfolder = "%s-%s" % (self.name, self.version)
        include_folder = "%s/gli" % source_subfolder
        self.copy("*.hpp", dst="include/gli", src=include_folder)
        self.copy("*.inl", dst="include/gli", src=include_folder)
        self.copy("manual.md", dst="licenses", src=source_subfolder)

    def package_id(self):
        self.info.header_only()

