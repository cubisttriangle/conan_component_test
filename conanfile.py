from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class my_unicode_libRecipe(ConanFile):
    name = "my_unicode_lib"
    version = "0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of my_unicode_lib package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def requirements(self):
        if self.settings.os == "Linux":
            self.requires("icu/73.1")
        else:
            raise Exception("Only Linux supported")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "my_unicode_lib")
        self.cpp_info.set_property("pkg_config_name", "my_unicode_lib")

        self.cpp_info.components["uni"].set_property("cmake_target_name", "my_unicode_lib::uni")
        self.cpp_info.components["uni"].set_property("pkg_config_name", "my_unicode_lib_uni")
        self.cpp_info.components["uni"].libs = ["uni"]
        self.cpp_info.components["uni"].requires = ["icu::icu-i18n"]
