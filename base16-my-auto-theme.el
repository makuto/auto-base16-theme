;;
;; Custom theme
;;

(require 'base16-theme)

(defvar base16-my-auto-colors
  '(:base00 "#000000"
    :base01 "#17181b"
    :base02 "#302429"
    :base03 "#c0c3b9"
    :base04 "#423439"
    :base05 "#4b4b4b"
    :base06 "#755253"
    :base07 "#656562"
    :base08 "#a2a7a1"
    :base09 "#8d646d"
    :base0A "#a2a7a1"
    :base0B "#c0c3b9"
    :base0C "#a2a7a1"
    :base0D "#755253"
    :base0E "#755253"
    :base0F "#a2a7a1")
  "All colors for Base16 Macoy are defined here.")

;; Define the theme
(deftheme base16-my-auto)

;; Add all the faces to the theme
(base16-theme-define 'base16-my-auto base16-my-auto-colors)

;; Mark the theme as provided
(provide-theme 'base16-my-auto)

(provide 'base16-my-auto-theme)

;;; base16-my-auto-theme.el ends here
