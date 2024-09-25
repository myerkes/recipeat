{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2024-09-25";
      url = "https://github.com/jpetrucciani/nix/archive/1bdbe64e49b5320557f7b5fccb3ba9d37307db09.tar.gz";
      sha256 = "197bpbf9fjkfi1fbl4mgk6abq23nlrksdwvi00rfm7i19c7k9fl4";
    })
    { }
}:
let
  name = "recipeat";

  python = pkgs.poetry-helpers.mkEnv {
    projectDir = ./.;
    python = pkgs.python312;
    extraOverrides = [
      (final: prev: {
        jstyleson = prev.jstyleson.overridePythonAttrs (_: { format = "setuptools"; });
      })
    ];
  };

  tools = with pkgs; {
    cli = [
      coreutils
      nixpkgs-fmt
    ];
    python = [
      ruff
      (poetry.override (_: { python3 = python312; }))
    ];
    scripts = pkgs.lib.attrsets.attrValues scripts;
  };

  scripts = with pkgs; { };
  paths = pkgs.lib.flatten [ (builtins.attrValues tools) ];
  env = python.env.overrideAttrs (_: {
    buildInputs = paths;
  });
in
(env.overrideAttrs (_: {
  inherit name;
  NIXUP = "0.0.7";
})) // { inherit scripts; }
