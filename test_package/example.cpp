#include <gli/sampler2d.hpp>
#include <glm/gtc/epsilon.hpp>

int main()
{
  int Error = 0;

  {
    gli::vec4 const Color(1.0f, 0.5f, 0.0f, 1.0f);
    gli::texture2d Texture(gli::FORMAT_R16_SFLOAT_PACK16, gli::texture2d::extent_type(1), 1);
    gli::detail::convertFunc<gli::texture2d, float, gli::u16, gli::defaultp, gli::tvec1, gli::detail::CONVERT_MODE_HALF, true>::write(Texture, gli::texture2d::extent_type(0), 0, 0, 0, Color);
    gli::vec4 Texel = gli::detail::convertFunc<gli::texture2d, float, gli::u16, gli::defaultp, gli::tvec1, gli::detail::CONVERT_MODE_HALF, true>::fetch(Texture, gli::texture2d::extent_type(0), 0, 0, 0);

    Error += gli::epsilonEqual(Texel.x, Color.x, 0.01f) ? 0 : 1;
  }

  return Error;
}